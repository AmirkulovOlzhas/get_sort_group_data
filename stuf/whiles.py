from os import listdir
from os.path import isfile, join

from rename_files_names import rename_all_files

mypath = r"D:\WA_photo\1"

all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("len", len(all_files))

rename_all_files(all_files, outside=True)
# taking updated photo names from folder
changed_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i, temp_value = 0, 0
for j in range(len(changed_files_name)):
    print(all_files[j], '  |  ', changed_files_name[j])
print('---------------- --------------- ----------------- -----------------')
