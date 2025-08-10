# Photo Sorter

A Python script that automatically organizes photos and videos by date into a clean folder structure.

## What it does

Takes messy photo collections from any folder (including subfolders) and organizes them into a structured format:

```
Organized Photos/
├── 2024/
│   ├── 08/
│   │   ├── 10/
│   │   │   ├── 14/30/22.jpg
│   │   │   └── 16/45/13.mp4
│   │   └── 11/
│   │       └── 09/15/33.jpg
│   └── 07/
│       └── 25/
│           └── 18/22/45.png
```

Photos are renamed to their timestamp and sorted into `YYYY/MM/DD/` folders based on when they were actually taken (using EXIF data).

## Features

- ✅ Uses file metadata to determine photo dates
- ✅ Handles multiple formats: JPG, JPEG, PNG, HEIC, MP4, MOV
- ✅ Works with external drives and SSDs  
- ✅ Recursive folder scanning (processes subfolders)

## How to use
1. **In main() add your folder of origin and destination**
   ```bash
   def main():
        global new_folder
        original_folder = "" #add your folder with unsorted photos
        new_folder = "" #folder where the photos will be sorted (must be outside of original_folder!!!)
        read_folders(original_folder)
   ```  
   - use "/Volumes/name or ssd or other" if using an ssd
   - use "/Users/name/Documents or other" if sorting on mac
2. **Run the script:**
   ```bash
   python3 photo_sorter.py
   ```


## Requirements

- Python 3.6+ (uses built-in `os` and `datetime` modules)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/klaud1a/photo-sorter.git
   cd photo-sorter
   ```

2. **Run the script:**
   ```bash
   python3 photo_sorter.py
   ```

No additional dependencies needed - uses only Python standard library!

## Why I built this

Tired of having thousands of unsorted photos scattered across different folders and devices? This script solves that problem by automatically organizing photos by the date they were actually taken, not when they were copied or modified.

Perfect for:
- Organizing photos from multiple devices (only works on Mac and external SSD (i don't have a Windows device to try it on))
- Cleaning up messy photo collections
- Preparing photos for backup or archival
- Anyone who takes lots of photos and wants them organized automatically

## About

This is my first Python project and GitHub repository! Built to solve my own photo organization problem - figured others might find it useful too.

*Created August 2025*

## Contributing

Found a bug or want to suggest an improvement? Feel free to open an issue or submit a pull request. This is a learning project, so constructive feedback is always welcome!