import os
import sys
import time
import logging
import shutil
import ntpath
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler, FileCreatedEvent

#directory to watch
path = os.path.expanduser("~/Desktop")
#where to move file
newPath = os.path.dirname("/home/richard/Documents/")


class Event(FileSystemEventHandler):
    def on_created(self, event):
        file , file_ext = os.path.splitext(event.src_path)

        if(file_ext == '.txt'):
            des = newPath + "/txt/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
        elif(file_ext == '.md'):
            des = newPath + "/md/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
        elif(file_ext == '.mp4' or file_ext == '.avi' or file_ext == '.mov' or file_ext == '.flv' or file_ext == '.wmv'):
            des = newPath + "/videos/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
        elif(file_ext == '.mp3' or file_ext == '.ogg' or file_ext == '.wma' or file_ext == '.flac' or file_ext == '.alac'):
            des = newPath + "/audio/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
        elif(file_ext == '.jpg' or file_ext == '.jpeg' or file_ext == '.png'):
            des = newPath + "/pictures/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
        else:
            des = newPath + "/" + ntpath.basename(event.src_path)
            shutil.move(event.src_path, des)
            print(des)
            
       

            
if __name__ == "__main__":
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