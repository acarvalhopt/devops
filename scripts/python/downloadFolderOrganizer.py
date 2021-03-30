from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#pip install watchdog to work.

import os
import json
import time

folder_to_track = "/Users/andrecarvalho/Downloads/test"
folder_destination = "/Users/andrecarvalho/Downloads/test"

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):

            if filename.endswith('.jpg'):
                new_destination = folder_destination + "/" + "images"
                print("folder_destination:", new_destination)
                if not os.path.isdir(str(new_destination)):
                    try:
                        os.mkdir(new_destination)
                    except OSError:
                        print ("Creation of the directory %s failed" % new_destination)
                    else:
                        print ("Successfully created the directory %s " % new_destination)
                print("files: ", filename)
                src = folder_to_track + "/" + filename
                new_destination = new_destination + "/" + filename
                os.rename(src, new_destination)

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