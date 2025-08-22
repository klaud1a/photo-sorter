#!/usr/bin/env python3
"""
Photo Sorter - Organize photos and videos by date
Author: Klaudia L - klaud1a
"""
import os
from pathlib import Path
from datetime import datetime
import exifread

def read_folders(folder):
    photo_extensions=['.jpg', '.jpeg', '.png', '.heic','.png','.mov','.mp4']
    for file_name in folder.iterdir(): #read all files
        if str(file_name)[0:2]=="._":
            pass
        else:
            if (file_name.suffix).lower() in photo_extensions: #finds if the file is image/is within the extentions
                photo_read_and_change(file_name) #takes photo to be manipulated
            elif file_name.is_dir(): #finds if file is a directory
                read_folders(file_name) #moves to directory to search it for photos'''
#original photo read change name
'''def photo_read_and_change(photo_name):
    stat = os.stat(photo_name) #reads photo data
    modified_time = (str(datetime.fromtimestamp(stat.st_mtime))).replace("-"," ").split() #finds date+time photo was modified and splits it into list
    create_nestedDir(modified_time[0],modified_time[1],modified_time[2]) #creates nested folder YYYY/MM/DD
    file_type ="." + photo_name.rsplit('.', 1)[-1]
    destination=new_folder+"/"+modified_time[0]+"/"+modified_time[1]+"/"+modified_time[2]+"/"+modified_time[3]+"(0)"
    i=0
    while True: #handles photos with same date/time by adding a number
        try:
            os.rename(photo_name,str(destination+file_type))
            break
        except:
            destination=destination[:-2]+i+")"
            i+=1'''
#new one

def photo_read_and_change(photo_name):
    with open(photo_name,"rb") as f:
        tags = exifread.process_file(f)
        EXIFdate=tags.get('EXIF DateTimeOriginal')
    if EXIFdate == None:
        osDate = os.stat(photo_name)
        osDate = str(datetime.fromtimestamp(osDate.st_mtime))
        osDate = osDate.split()
        date=osDate[0].replace("-","/")
        time=osDate[1]
    else:
        EXIFdate=str(EXIFdate).split()
        date=EXIFdate[0].replace(":","/")
        time=EXIFdate[1]
    
    path=new_folder / date
    Path.mkdir(path, parents=True, exist_ok=True)
    destination = path / (time + photo_name.suffix)
    counter=1
    while destination.exists():
        stem = time + f"_{counter}"
        destination = path / (stem + photo_name.suffix)
        counter += 1
    Path.rename(photo_name,destination)

def main():
    global new_folder
    #original_folder = Path(input("Please add file path to the folder with photos (refer to README for more info)\n")) #add your folder with unsorted photos
    #new_folder = Path(input("Please add file path to the folder you want the photos in (refer to README for more info)\n"))#folder where the photos will be sorted (must be outside of original_folder!!!)
    original_folder=Path("/Users/klaudia.lalova/Desktop/test-photos")
    new_folder=Path("/Users/klaudia.lalova/Desktop/new")
    read_folders(original_folder)

if __name__ == "__main__":
    main()