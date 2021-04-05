from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#pip3 install watchdog to work.

import os
import json
import time


def organize(src, dstFolder,filename):
    new_destination = folder_destination + "/" + dstFolder
    try:
        if not os.path.isdir(str(new_destination)):
            print("[INFO] - Destination folder doesn't exist, creating: " + new_destination)
            os.mkdir(new_destination)
        print("[INFO] - Moving file " + filename + " to: ", new_destination)
        src = src + "/" + filename
        new_destination = new_destination + "/" + filename
        os.rename(src, new_destination)

    except OSError:
        print ("[ERROR] - Failed to move file: " + filename)
    else:
        print ("[INFO] - Moved file: " + filename + " sucessfully!")

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        
        for filename in os.listdir(folder_to_track):
            saved = False
            
            for key,value in dictRootFolders.items():
                for item in value:
                    #save screenshots in a different directory.
                    if filename.startswith(dictRootFolders['printscreen'][0]) and not saved: 
                        organize(folder_to_track,"printscreen",filename)
                        saved = True
                    elif (filename.endswith(item.upper()) or filename.endswith(item.lower())) and not saved:
                        organize(folder_to_track,key,filename)
                        saved = True
            #if not in our dictionarie of extensions save in "others" folder.     
            if filename not in dictRootFolders.keys() and not saved:
                organize(folder_to_track,"others",filename)
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