import time
import os
import shutil
from watchdog.Observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\\Users\\HP\\Downloads"

source = "main.txt"

dest = "newfile.txt"

os.rename ("newfile.txt")