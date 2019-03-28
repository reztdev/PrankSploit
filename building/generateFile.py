#!/usr/bin/python
import sys
import os
import time

file_build = sys.argv[1]

try:
    print("\t\t=======================================")
    print("\t\t[  ** Generate File to Executable **  ]")
    print("\t\t=======================================")
    print("\n")
    print("Started building file to executable for windows...")
    time.sleep(3)
    print("Loading to running this pyinstaller....")
    time.sleep(3)
    print("Please wait to several few minutes...")
    time.sleep(3)
    os.system('pyinstaller -F {files}'.format(files=file_build))
except KeyboardInterrupt:
    print("User Interrupt...\nExiting!!!")
    sys.exit()
