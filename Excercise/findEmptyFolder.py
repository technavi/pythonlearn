import os
import shutil
lookuppath='D:\\IMAGES\\01 Photos\\01 Photos All'

 
# Create a List    
listOfEmptyDirs = list()
# Iterate over the directory tree and check if directory is empty.
for (dirpath, dirnames, filenames) in os.walk(lookuppath):
    # print(dirpath) 
    print(len(dirnames),len(filenames),dirnames,filenames)
    # if len(dirnames) == 0 and len(filenames)==1 and filenames[0] == 'Thumbs.db' :
    if len(dirnames) == 0 and len(filenames)==0:
        print("in if")
        listOfEmptyDirs.append(dirpath)

for d in listOfEmptyDirs:
    print(d)
    # os.rmdir(d)
    shutil.rmtree(d)

