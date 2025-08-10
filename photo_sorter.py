#!/usr/bin/env python3
"""
Photo Sorter - Organize photos and videos by date
Author: Klaudia L - klaud1a
"""
import os
from datetime import datetime

def read_folders(path):
    photo_extensions=['.jpg', '.jpeg', '.png', '.heic','.png','.mov','.mp4']
    for x in os.listdir(path): #read all files
        if x[0:2]=="._":
            pass
        else:
            x=path+"/"+str(x) #make sure the x is full not relative path
            if x.lower().endswith(tuple(photo_extensions)): #finds if the file is image
                photo_read_and_change(x) #takes photo to be manipulated
            elif os.path.isdir(x): #finds if file is a directory
                read_folders(x) #moves to directory to search it for photos

def photo_read_and_change(name):
    stat = os.stat(name) #reads photo data
    modified_time = (str(datetime.fromtimestamp(stat.st_mtime))).replace("-"," ").split() #finds date+time photo was modified and splits it into list
    create_nesteddir(new_folder,modified_time[0],modified_time[1],modified_time[2]) #creates nested folder YYYY/MM/DD
    file_type ="." + name.rsplit('.', 1)[-1]
    dest=new_folder+"/"+modified_time[0]+"/"+modified_time[1]+"/"+modified_time[2]+"/"+modified_time[3]+"(0)"
    i=0
    while True: #handles photos with same date/time by adding a number
        try:
            os.rename(name,str(dest+file_type))
            break
        except:
            dest=dest[:-2]+i+")"
            i+=1

def create_nesteddir(new,y,m,d): #creates nested folder structure
    x=new
    z=[y,m,d,""]
    for i in range(4):
        try: #handeling already existing folders
            os.mkdir(x)
        except:
            pass
        x=x+"/"+z[i]

def main():
    global new_folder
    original_folder = "" #add your folder with unsorted photos
    new_folder = "" #folder where the photos will be sorted (must be outside of original_folder!!!)
    read_folders(original_folder)

if __name__ == "__main__":
    main()