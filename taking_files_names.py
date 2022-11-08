import os
from os import listdir
from os.path import isfile, join

mypath = r"C:\Users\OFFICE\Desktop\test"

counter = {"17 Мкр": 0,
           "Касирет": 0,
           "Алатау": 0,
           "Нурсат": 0,
           "Победа": 0
           }


def rename_file(this_line):
    temp_line_name = this_line.replace(' (', '-')
    temp_line_name = temp_line_name.replace(')', '')
    os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)


# taking photo names from folder
all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(len(all_files_name))

# delete () to correct sort files
for line in all_files_name:
    if ('(' in line) & (')' in line):
        rename_file(line)

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
