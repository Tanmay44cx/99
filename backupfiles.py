import os 
import shutil
destination = input("Enter The Destination")
source = input("Enter the Folder that has to be copied")
source=source+'/'
destination=destination+'/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy(source+file,destination)
