from os import listdir
from os.path import isfile, join, isdir

import pandas as pd
import matplotlib.pyplot as plt


def show_stat(result_dict):
    for folder_name, values in result_dict.items():
        contact_count = {}
        for name, count in values.items():
            contact_count.update({name: count['count']})
        print(contact_count)
        df = pd.Series(contact_count)
        plt.figure(figsize=(6, 4))
        plt.title(folder_name)
        plt.bar(x=df.index, height=df)
        plt.xticks(rotation=13)
        plt.show()


result = {}
while True:
    try:
        group_index = int(input("0-1-2: "))
        if group_index in [0, 1, 2]:
            break
    except:
        print('wrong')

group_names = ["Парки", "Енбекшинский", "Абайский"]
mypath = "D:\\Фото архив\\" + group_names[group_index]
all_folders_name = [f for f in listdir(mypath) if isdir(join(mypath, f))]

for folder in all_folders_name:
    path = mypath + '\\' + folder
    result.update({folder: {}})
    all_files_name = [f for f in listdir(path) if isfile(join(path, f))]
    times = []
    for file in all_files_name:
        if file[-4:] not in ['.txt', '.mp4']:
            temp_name = file.split(' ')
            temp_name[1] = temp_name[1].replace('-', '')
            if temp_name[1] in result[folder]:
                result[folder][temp_name[1]]['count'] += 1
                result[folder][temp_name[1]]['time'].append(temp_name[0].replace('_', ':'))
            else:
                print(file)
                result[folder].update({temp_name[1]: {'count': 1, 'time': [temp_name[0].replace('_', ':')]}})

show_stat(result)
# print(result)
