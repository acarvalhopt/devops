from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#pip3 install watchdog to work.

import os
import json
import time

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
            saved = False
            
            for key,value in dictRootFolders.items():
                for item in value:
                    #save screenshots in a different directory.
                    if filename.startswith(dictRootFolders['printscreen'][0]) and not saved: 
                        organize("printscreen",filename)
                        saved = True
                    elif (filename.endswith(item.upper()) or filename.endswith(item.lower())) and not saved:
                        organize(key,filename)
                        saved = True
            #if not in our dictionarie of extensions save in "others" folder.     
            if filename not in dictRootFolders.keys() and not saved:
                organize("others",filename)
                saved = True


folder_to_track = "/Users/andrecarvalho/Downloads"
folder_destination = "/Users/andrecarvalho/Downloads"
dictRootFolders = { 'images':['.jpeg','.jpg','.png','.gif'],
                    'pdf':['.pdf'],
                    'office':['.csv','.xls','.xlsx'],
                    'zip':['.zip','.tar.bz2','.tar.gz','.tgz','.rar'],
                    'videos':['.mp4','.mov'],
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