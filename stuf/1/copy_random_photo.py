import os
from shutil import copy2

# Set the source and destination folders
src_folder = r'D:\Фото архив\Туран\1-1-2023'
dst_folder = r"C:\Users\OFFICE\Desktop\бегара"

# Set the specific word to search for in the file name
specific_word = "Мражан"

# Get a list of all files in the source folder
all_files = os.listdir(src_folder)

# Filter the list to only include image files with specific word in the file name
image_files = [f for f in all_files if (f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.gif')) and specific_word in f]

# Select 3 random files from the list
selected_files = random.sample(image_files, 3)

# Copy the selected files to the destination folder
for file in selected_files:
    src = os.path.join(src_folder, file)
    dst = os.path.join(dst_folder, file)
    copy2(src, dst)