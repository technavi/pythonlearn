import os
import filecmp
from datetime import datetime
import numpy as np 
import shutil  

# function to get unique values 
def unique(list1): 
    x = np.array(list1) 
    return  np.unique(x) 

lookuppath='D:\\IMAGES\\01 Photos\\01 Photos All'

fType="V"

if(fType=="V"):
    accepted_extensions = ["3gp","avi","AVI",":3GP","MP4","mpg","DAT","mp4","AVI","avi","MOV","mov"]
    destDir='G:\\01 Photos\\04 Pictures - OLD\\MoveHere\\Videos'
else:
    accepted_extensions = ["JPG","jpg", "png","JPG",'bmp',"CR2","png","PNG","jpeg","JPEG"]
    destDir='G:\\01 Photos\\04 Pictures - OLD\\MoveHere'

duplicatePath='F:\\RND\\Duplicate'
# return           
# entries = os.scandir('F:\\Movies')
listDirs = os.listdir(lookuppath)
     
uniqueFoldersToCreate=[]
for item in listDirs:
    folderpath= lookuppath +"\\" + item
    entries = [fn for fn in os.scandir(folderpath) if fn.name.split(".")[-1] in accepted_extensions] 
    # uniqueFolderName=unique(entries[])
    # print(folderpath)
    # Get file properties of Create Date and Prepare Distinct list to create folder

    for item in entries:
        fileName=item.name
        if(item.is_file()):
            sourcePath=item.path
            # print(item.name,item.path)
            dateTime=datetime.fromtimestamp(item.stat().st_mtime)
            dateFolderName=dateTime.strftime('%Y-%m-%d')
            # print(dateTime.strftime('%Y-%m-%d %H:%M:%S'))
            # print(fileName,dateFolderName)
            uniqueFoldersToCreate.append(dateFolderName)
            # Create Directory
            try: 
                destPath = os.path.join(destDir, dateFolderName)
                # print('destPath',destPath) 
                os.makedirs(destPath, exist_ok = True)
                # print(sourcePath,destPath + "\\" + item.name)
                result= False 
                destFilePath=destPath + '\\' + item.name
                try:
                    # print(os.path.exists(destFilePath))
                    if os.path.exists(destFilePath):
                        result = filecmp.cmp(sourcePath,destFilePath)
                        print("exists",result)
                        # print(sourcePath,destPath + '\\' + item.name,result)
                    else:
                        result=False
                        print("not exists",  result)
                except FileExistsError as error:
                    result=True  
                    print('error',error)   
                # print(not result)
                # print("asdf,",bool(result))
                if(not bool(result)):
                    print("Move to new location", destPath)
                    dest = shutil.move(sourcePath, destPath)
                else:
                    dpath=duplicatePath + '\\' + item.name
                    destDup=shutil.move(sourcePath,dpath)
                    print("Moved to DUPLICATE PATH - ", dpath)
  
                # # if(not bool(result)): 

                # destFilePath=destPath + '\\' + item.name
                # if not os.path.exists(destFilePath):
                #      dest = shutil.move(sourcePath, destPath)
                # else:
                #     print("File already exists " + destFilePath)
                #     dest = shutil.move(sourcePath, destPath)
                    
            except OSError as error:
                print(error)                
        # Move File Code here




        
    
    # print(unique(uniqueFoldersToCreate)) 
       

# basepath='F:\\HD'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)

# Compare files binary
# result=filecmp.cmp('F:\Movies\Dracula (2020) S01E01 Hindi Eng 720p WEB-DL @UlluWeb_Series.mkv', 'F:\Movies\Dracula (2020) S01E01 Hindi Eng 720p WEB-DL @UlluWeb_Series.mkv') 
# print(result)