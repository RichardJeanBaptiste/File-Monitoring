import os
import sys
import time
import logging
import shutil
import ntpath
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler, FileCreatedEvent

#move file on creation
newPath = os.path.dirname("/home/richard/Documents/")

class Event(FileSystemEventHandler):
    def on_created(self, event):
        des = newPath + "/" + ntpath.basename(event.src_path)
        shutil.move(event.src_path, des)
        print(des)

        
    
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = os.path.expanduser("~/Desktop")
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print('Watchdog Started')
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
            print('Watchdog Closing')
            observer.stop()
    observer.join()
