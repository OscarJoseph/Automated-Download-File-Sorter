from tkinter import PhotoImage
from cv2 import FileNode_MAP
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            #Sort Music Files
            if filename.endswith((".mp3", ".wav", ".flac")):
                src = folder_to_track + "/" + filename
                new_destination = music_folder + "/" + filename
                os.rename(src, new_destination)
            #Sort Photo Files
            elif filename.endswith((".jpg", ".png", ".jpeg")):
                src = folder_to_track + "/" + filename
                new_destination = photo_folder + "/" + filename
                os.rename(src, new_destination)
            #Sort Reading FIles
            elif filename.endswith((".pdf", ".txt", ".docx", ".zip", ".rar")):
                src = folder_to_track + "/" + filename
                new_destination = document_folder + "/" + filename
                os.rename(src, new_destination)
            #Sort Installation Files
            elif filename.endswith(".exe"):
                src = folder_to_track + "/" + filename
                new_destination = installation_folder + "/" + filename
                os.rename(src, new_destination)

#Directories of the destination files                    
installation_folder = "/Users/oscar/Documents/Install"
document_folder = "/Users/oscar/Documents/Assorted"
folder_to_track = "/Users/oscar/Downloads"
music_folder = "/Users/oscar/Music/Assorted"
photo_folder = "/Users/oscar/Pictures/Assorted"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
