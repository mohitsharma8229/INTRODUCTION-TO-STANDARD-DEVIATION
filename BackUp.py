import os
import shutil
source=input("enter the source folder name")
dest=input("enter the destination folder")
source=source+'/'
dest=dest+'/'
listofFile=os.listdir(source)
for file in listofFile:
    shutil.copy((source+file),dest)