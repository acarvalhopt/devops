import tableauserverclient as TSC
import os
import zipfile
import re
from git import Repo
import git
from git import Git
from datetime import datetime, timedelta
import configparser    
import codecs
import keyring
import getpass
import logging
import logConfig
import argparse
import shutil

# set environment Variable
environment = ""
#parsing credentials in config.ini
cfg = configparser.ConfigParser()
cfg.read('config.ini') 

#set up logging 
logger = logging.getLogger(__name__)

#set up arguments for updating password and incremental or full load backup
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required = True)
parser.add_argument('-p', '--password', choices = ['a', 't', 'g'], help = 'Set password for [a]ll, [t]ableau server, or [g]it and the [e]nvironment')
parser.add_argument('-e', '--environment', choices = ['dev', 'pp', 'prd'], help = 'Choose which environment you will version')
group.add_argument('-i', '--incremental', type = int, nargs = '?', const = 1, metavar = '<hours>', help = 'Set the time period in hours to scan for any changes in Tableau Server, default is 1 aka scan for changes made in the last hour')
group.add_argument('-f', '--full-load', action = 'store_true', help = 'Back up all workbooks and datasources regardless of last updated time')
args = parser.parse_args()

os.system('git config --global core.longpaths true')

def main():

    try:

        tableauPassword, gitPassword, environment, env_site_id = getCreds()

        logger.info('Preparing Backup')

        #setting up tableau login credentials
        tableau_auth = TSC.TableauAuth(cfg['tableauServer']['user'], tableauPassword, site_id=env_site_id)
        server = TSC.Server(cfg['tableauServer']['url'], use_server_version = True)

        firstTime = False
        
        #check if there is git repo, if not clone the repository
        oPath = cfg['git']['projectName']
	
        #if os.path.isdir(oPath) is False:
        #    Repo.clone_from('http://'+cfg['git']['login']+':'+gitPassword+'@'+cfg['git']['url'].split('://', 1)[1], oPath)
        #    firstTime = True 

        if os.path.isdir(oPath) is False:
            git_ssh_identity_file = os.path.expanduser('/home/.ssh/id_rsa')
       	    git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file

            with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
                Repo.clone_from('git@git_url/repository.git', oPath, branch='develop')
                firstTime = True

	
        repo = git.Repo(oPath)
        oPath = oPath + "/" +environment

        #logging into tableau server
        server.auth.sign_in(tableau_auth)
        
        #setting time stamp for one hour previous from when this script is run 
        currentTime = datetime.now()
        downloadChangesSince = (datetime.fromtimestamp((currentTime.timestamp() - args.incremental*3600)).replace(microsecond = 0)).isoformat() + 'Z'

        if firstTime is True or args.full_load == True:
            downloadChangesSince = '2000-01-01T00:00:00Z'
        
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.UpdatedAt,
                                    TSC.RequestOptions.Operator.GreaterThanOrEqual,
                                    downloadChangesSince))

        remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
        
        #iterating through each site on tableau
        for site in TSC.Pager(server.sites):
                
            logger.info('Backing up workbooks and datasources under the {} site changed after {}'.format(site.name, downloadChangesSince))
                
            #logging into the specific site
            tableau_auth1 = TSC.TableauAuth(cfg['tableauServer']['user'], tableauPassword, site_id = site.content_url)
            server.auth.sign_in(tableau_auth1)
            
            sPath = os.path.join(oPath, site.name.translate(remove_punctuation_map))
            if os.path.isdir(sPath) is False:
                os.makedirs(sPath)

            #iterating through each workbook in the specified site to download and extract
            for workbook in TSC.Pager(server.workbooks, req_option):
                
                workbookName = workbook.project_name.translate(remove_punctuation_map)
                xPath = os.path.join(sPath, workbookName)
                
                if os.path.isdir(xPath) is False:
                    os.makedirs(xPath)

                file_path = server.workbooks.download(workbook.id, filepath = xPath, no_extract = True)

                print('----     path    ----------')
                print('----     '+ file_path)
                print('----     '+ site.name)
                print('----     '+ workbookName)
                print('----     '+ workbook.project_id)
                print('----     '+ workbook.id)
                print('---     /path-----------')
                
                extractWorkbook(file_path, site.name, workbookName, workbook.project_id, workbook.id, os.path.basename(file_path), xPath)

            #iterating through each datasource in the specified site to downlad and extract
            for datasources in TSC.Pager(server.datasources, req_option):
            
                datasourcesName = datasources.project_name.translate(remove_punctuation_map)
                dPath = os.path.join(sPath, datasourcesName)

                if os.path.isdir(dPath) is False:
                    os.makedirs(dPath)

                file_path = server.datasources.download(datasources.id, filepath = dPath, include_extract = False)
                extractDatasource(file_path, site.name, datasourcesName, datasources.project_id, datasources.id, os.path.basename(file_path), dPath)
        
        #pushing changes to git and timestamping when this script was run
        print(repo.git.status())
        if "nothing to commit" not in repo.git.status():
            repo.git.add('.')
            repo.git.commit(m = "backup of" + environment + ": " + currentTime.strftime('%Y-%m-%d %H-%M-%S'))
            repo.git.push('origin')
            print("backed up to git")
        
        logger.info('Backup Complete')
        server.auth.sign_out()

    except:
        logging.exception('error')
        pass

#function for extracting workbooks and renaming as: siteName\workbookProjectName_[worbookProjectID]\workbookName_<workbookID>
def extractWorkbook(file_path, site_name, project_name, project_id, workbook_id, workbook_name, oPath):
    if re.match(r'.*\.twbx$', file_path):
        print(file_path)
        zip_ref = zipfile.ZipFile(file_path,'r') 
        print(zip_ref)
        for info in zip_ref.infolist():
            if re.match(r'.*\.twb$', info.filename):
                nName = workbook_name.replace('.twbx', '_'+workbook_id+'.twb')
                print(nName)
                with open(os.path.abspath(os.path.join(oPath, nName)), 'wb') as f:
                    f.write(zip_ref.read(info))
                zip_ref.close()
                os.remove(file_path)

    elif re.match(r'.*\.twb$', file_path):
        pName = os.path.splitext(file_path)[0] + ('_'+workbook_id+'.twb')
        #shutil.move(file_path, u"\\\\?\\" + pName)
        shutil.move(file_path, pName)


#function for extracting datasources and renaming as: siteName\datasourceProjectName_[datasourceID]\datasourceName_<datasourceID>    
def extractDatasource(file_path, site_name, project_name, project_id, datasources_id, datasources_name, oPath):
    if re.match(r'.*\.tdsx$', file_path):
        zip_ref = zipfile.ZipFile(file_path,'r')
        for info in zip_ref.infolist():
            if re.match(r'.*\.tds$', info.filename):
                yName = datasources_name.replace('.tdsx', '_'+datasources_id+'.tds')
                with open(os.path.join(oPath, yName), 'wb') as f:
                    f.write(zip_ref.read(info))
                zip_ref.close()
                os.remove(file_path)

    elif re.match(r'.*\.tds$', file_path):
        wName = os.path.splitext(file_path)[0] + ('_'+datasources_id+'.tds')
        shutil.move(file_path, "\\\\?\\" + wName)
        #shutil.move(file_path, "\\\\?\\" + wName)
        shutil.move(file_path, wName)

#getting login credentials from config.ini and command line
def getCreds():
    service_id = 'TableauBackup'
    
    if args.environment == 'dev':
        environment = args.environment
        env_site_id='sandbox'

    #get password for tableau server
    if not keyring.get_password(service_id, cfg['tableauServer']['user']):
        keyring.set_password(service_id, cfg['tableauServer']['user'], getpass.getpass('Enter Tableau Server Password For {}: '.format(cfg['tableauServer']['user'])))

    #get password for git
    #if not keyring.get_password(service_id, cfg['git']['login']):
    #    keyring.set_password(service_id, cfg['git']['login'], getpass.getpass('Enter Git Password For {}: '.format(cfg['git']['login'])))

    #update password depending on arguments from commandline
    #if args.password == 'g':
    #    keyring.set_password(service_id, cfg['git']['login'], getpass.getpass('Enter New Git Password For {}: '.format(cfg['git']['login'])))
    elif args.password == 't':
        keyring.set_password(service_id, cfg['tableauServer']['user'], getpass.getpass('Enter New Tableau Server Password For {}: '.format(cfg['tableauServer']['user'])))
    elif args.password == 'a':
        keyring.set_password(service_id, cfg['tableauServer']['user'], getpass.getpass('Enter New Tableau Server Password For {}: '.format(cfg['tableauServer']['user'])))
    #    keyring.set_password(service_id, cfg['git']['login'], getpass.getpass('Enter New Git Password For {}: '.format(cfg['git']['login'])))

    return (keyring.get_password(service_id, cfg['tableauServer']['user']), keyring.get_password(service_id, cfg['git']['login']),environment,env_site_id)   

main()
