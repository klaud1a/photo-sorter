#!/usr/bin/env python3
"""
Photo Sorter - Organize photos and videos by date
Author: Klaudia L - klaud1a
"""
import os
import pathlib
from datetime import datetime

def read_folders(path):
    photo_extensions=['.jpg', '.jpeg', '.png', '.heic','.png','.mov','.mp4']
    for file_name in os.listdir(path): #read all files
        if file_name[0:2]=="._":
            pass
        else:
            file_name=path+"/"+str(file_name) #make sure the file name is full not relative path
            if file_name.lower().endswith(tuple(photo_extensions)): #finds if the file is image/is within the extentions
                photo_read_and_change(file_name) #takes photo to be manipulated
            elif os.path.isdir(file_name): #finds if file is a directory
                read_folders(file_name) #moves to directory to search it for photos

def photo_read_and_change(photo_name):
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
            i+=1

def create_nestedDir(y,m,d): #creates nested folder structure
    new_folderCopy=new_folder
    z=[y,m,d,""]
    for i in range(4):
        try: #handeling already existing folders
            os.mkdir(new_folderCopy)
        except:
            pass
        new_folderCopy=new_folderCopy+"/"+z[i]

def main():
    global new_folder
    original_folder = input("Please add file path to the folder with photos (refer to README for more info)\n") #add your folder with unsorted photos
    new_folder = input("Please add file path to the folder you want the photos in (refer to README for more info)\n")#folder where the photos will be sorted (must be outside of original_folder!!!)
    read_folders(original_folder)

if __name__ == "__main__":
    main()