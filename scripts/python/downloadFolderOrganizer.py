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

#TODO:
#change Captura to value of 'printscreen'
#remove RootFolders
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        
        for filename in os.listdir(folder_to_track):
            saved = False
            #save screenshots in a different directory.
            for key,value in dictRootFolders.items():
                for item in value:
                    if filename.startswith(dictRootFolders['printscreen'][0]) and not saved: 
                        organize("printscreen",filename)
                        saved = True
                    elif (filename.endswith(item.upper()) or filename.endswith(item.lower())) and not saved:
                        organize(key,filename)
                        saved = True

            # if it's not a screenshot, it's not in our dictionary and it's not a rootFolder should go to "others"
            if filename not in rootFolders and not saved:    
                organize("others",filename)

rootFolders = ['images','pdf','csv','printscreen','zip','videos','xml','sh','python','sql','properties','installers','yaml','others','txt','certs']
dictRootFolders = { 'images':['.jpeg','.jpg','.png','.gif'],
                    'pdf':['.pdf'],
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
                    'certs':['.crt','.pub','.pem','.key'],
                    'printscreen':['Captura'],
                    'others':['otherExtensions']
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