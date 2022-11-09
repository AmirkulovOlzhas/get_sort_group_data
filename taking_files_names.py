import os
from os import listdir
from os.path import isfile, join
from stuf.delete_parentheses import rename_all_files

mypath = r"C:\Users\OFFICE\Desktop\test"

counter = {"17 Мкр": 0,
           "Касирет": 0,
           "Алатау": 0,
           "Нурсат": 0,
           "Победа": 0
           }

# taking photo names from folder
all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(len(all_files_name))

rename_all_files(all_files_name)

# taking updated photo names from folder
all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i, temp_value = 0, 0

# rename
with open('stuf/park_mes_name.txt', 'r', encoding='utf8') as f:
    for line in f:
        try:
            for key, value in counter.items():
                if key == line.replace('\n', ''):
                    counter[key] += 1
                    temp_value = counter[key]
            os.rename(mypath + '\\' + all_files_name[i],
                      mypath + '\\' + line.replace('\n', '') + f' - {temp_value}.jpeg')
        except Exception as e:
            print(e)
        i += 1
