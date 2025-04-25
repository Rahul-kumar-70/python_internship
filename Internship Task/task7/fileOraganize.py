"""
Problem Statement:Develop a Python script that organizes files in a specified
directory based on their file types.
Steps to Complete:
1. Use the os library to navigate and manipulate directories.
2. Create subdirectories for different file types (images, documents, etc.).
3. Move files into their respective folders.
Tools/Datasets/Platforms:
 Programming Language: Python 3.x.
"""
import os
import shutil


FILE_TYPE_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPE_MAP.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

def organize_files(directory):
    if not os.path.isdir(directory):
        print("Invalid directory!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            folder_name = get_folder_name(ext)

            target_folder = os.path.join(directory, folder_name)
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, filename)
            shutil.move(file_path, target_path)
            print(f"Moved: {filename} → {folder_name}/")

directory_path = input("Enter the path of the directory to organize: ")
organize_files(directory_path)
