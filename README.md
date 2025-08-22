# Photo Sorter

A Python script that automatically organizes photos and videos by date into a clean folder structure.

## What it does

Takes messy photo collections from any folder (including subfolders) and organizes them into a structured format:

```
Organized Photos/
├── 2024/
│   ├── 08/
│   │   ├── 10/
│   │   │   ├── 14:30:22.jpg
│   │   │   ├── 14:30:22_1.jpg    (duplicate handling)
│   │   │   └── 16:45:13.mp4
│   │   └── 11/
│   │       └── 09:15:33.jpg
│   └── 07/
│       └── 25/
│           └── 18:22:45.png
```

Photos are renamed to their timestamp and sorted into `YYYY/MM/DD/` folders based on when they were actually taken (using EXIF data).

## Features

- ✅ **EXIF data reading** - Gets actual photo capture date/time
- ✅ **Smart fallback** - Uses file modification date when EXIF is missing
- ✅ **Duplicate handling** - Automatically adds counters (_1, _2, etc.) for duplicates
- ✅ **Multiple formats** - JPG, JPEG, PNG, HEIC, MP4, MOV
- ✅ **External drive support** - Works with SSDs and external storage
- ✅ **Recursive scanning** - Processes all subfolders automatically  
- ✅ **Mac system file filtering** - Skips hidden system files (._*)

## How to use

**Interactive mode (recommended):**
```bash
python3 photo_sorter.py
```
The script will prompt you for:
- Source folder path (where your unsorted photos are)
- Destination folder path (where organized photos will go)

**Path examples:**
- External SSD: `/Volumes/YourSSDName/Photos`
- Mac Documents: `/Users/yourusername/Documents/Photos`
- Desktop: `/Users/yourusername/Desktop/UnsortedPhotos`

**Important:** Destination folder must be outside the source folder to avoid conflicts!

## Requirements

- Python 3.6+
- `exifread` library for EXIF data extraction

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/klaud1a/photo-sorter.git
   cd photo-sorter
   ```

2. **Install dependencies:**
   ```bash
   pip install exifread
   ```

3. **Run the script:**
   ```bash
   python3 photo_sorter.py
   ```

## How it works

1. **Scans source folder** recursively for photos/videos
2. **Reads EXIF data** to get original capture date/time
3. **Falls back to file date** if EXIF data is missing (social media downloads, etc.)
4. **Creates folder structure** based on date (YYYY/MM/DD)
5. **Renames files** to timestamp format (HH:MM:SS.extension)
6. **Handles duplicates** automatically with counters
7. **Moves files** to organized destination

## Why I built this

Tired of having thousands of unsorted photos scattered across different folders and devices? This script solves that problem by automatically organizing photos by the date they were actually taken, not when they were copied or modified.

Perfect for:
- Organizing photos from multiple devices  
- Cleaning up messy photo collections
- Preparing photos for backup or archival
- Processing photos from social media (handles missing EXIF data)
- Anyone who takes lots of photos and wants them organized automatically

**Tested on:** macOS with external SSDs. Should work on Windows/Linux but not tested.

## About

This is my first Python project and GitHub repository! Built to solve my own photo organization problem - figured others might find it useful too.

The project evolved from basic file operations to include EXIF reading, pathlib usage, and robust duplicate handling based on community feedback and real-world testing.

*Created August 2025*

## Contributing

Found a bug or want to suggest an improvement? Feel free to open an issue or submit a pull request. This is a learning project, so constructive feedback is always welcome!

**Known limitations:**
- Only tested on macOS
- Requires manual path input (no GUI)
- Moves files (doesn't copy) - make backups first!
- May display "File format not recognized" messages for video files - this is normal and doesn't affect functionality. The script will automatically use file dates for videos and other non-image formats.