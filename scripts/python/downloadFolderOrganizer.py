from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#pip3 install watchdog to work.

import os
import json
import time

folder_to_track = "/Users/andrecarvalho/Downloads"
folder_destination = "/Users/andrecarvalho/Downloads"

def createDstFolder(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def moveFile(path,dst,filename):
    print("files: ", filename)
    src = path + "/" + filename
    dst = dst + "/" + filename
    try:
        os.rename(src, dst)
    except Exception:
        print ("Move %s failed" % src)
    else:
        print ("Move Success %s " % src)

def organize(dstFolder,filename):
    new_destination = folder_destination + "/" + dstFolder
    if not os.path.isdir(str(new_destination)):
        createDstFolder(new_destination)
    print("Moving to:", new_destination)
    moveFile(folder_to_track,new_destination,filename)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.PNG') or filename.endswith('.GIF'):
                if filename.startswith('Captura'):
                    organize("printscreen",filename)
                else:
                    organize("images",filename)
            elif filename.endswith('.pdf') or filename.endswith('.PDF'):
                organize("pdf",filename)
            elif filename.endswith('.csv') or filename.endswith('.xls') or filename.endswith('.xlsx'):
                organize("csv",filename)
            elif filename.endswith('.zip') or filename.endswith('.tar.bz2') or filename.endswith('.tar.gz') or filename.endswith('.tgz') or filename.endswith('.rar'):
                organize("zip",filename)
            elif filename.endswith('.mp4'):
                organize("videos",filename)
            elif filename.endswith('.xml'):
                organize("xml",filename)
            elif filename.endswith('.sh'):
                organize("sh",filename)
            elif filename.endswith('.py'):
                organize("python",filename)
            elif filename.endswith('.sql'):
                organize("sql",filename)
            elif filename.endswith('.properties') or filename.endswith('.conf'):
                organize("properties",filename)
            elif filename.endswith('.dmg') or filename.endswith('.pkg'):
                organize("installers",filename)
            elif filename.endswith('.yaml') or filename.endswith('.yml'):
                organize("yaml",filename)
            elif filename.endswith('.rtf') or filename.endswith('.txt'):
                organize("txt",filename)
            elif filename.endswith('.crt') or filename.endswith('.pub') or filename.endswith('.pem') or filename.endswith('.key'):
                organize("certs",filename)
            else:
                if filename not in rootFolders:    
                    organize("others",filename)

rootFolders = ['images','pdf','csv','printscreen','zip','videos','xml','sh','python','sql','properties','installers','yaml','others','txt','certs']

dictRootFolders = { 'images':['.jpeg','.jpg','.png','.gif','.JPEG','.JPG','.PNG','.GIF'],
                    'pdf':['.pdf','.PDF'],
                    'office':['.csv','.xls','xlsx'],
                    'zip':['.zip','.tar.bz2','.tar.gz','.tgz','.rar'],
                    'videos':['.mp4'],
                    'xml':['.xml'],
                    'sh':['.sh'],
                    'python':['.py'],
                    'sql':['.sql'],
                    'properties':['.conf','.properties'],
                    'installers':['.dmg','.pkg'],
                    'yaml':['.yaml','.yml'],
                    'txt':['.rtf','.txt'],
                    'certs':['.crt','.pub','.pem','.key']
                    }


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()