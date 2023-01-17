import os
import sys
import shutil
from os import listdir
from os.path import isfile, join
from folder_works import copy_address_text


def get_files_name():
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]


def rename_file(this_line):
    try:
        temp_line_name = this_line.replace(' (', '')
        temp_line_name = temp_line_name.replace(')', '')
        if temp_line_name[-4:] == '.mp4':
            temp_line_name = temp_line_name.replace('Video', 'Image')
        else:
            temp_line_name = temp_line_name
        os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)
    except:
        pass


def convert_all_files(afn):
    # to correct sort list
    for this_line in afn:
        rename_file(this_line)


def create_new_folder(last_folder):
    temp_folder_name = last_folder.split(r'\\')[-1]
    temp_day = temp_folder_name.split('-')[0]
    if temp_day == '1':
        temp_mounth = temp_folder_name.split('-')[1]
        last_folder = last_folder.replace(temp_day + '-' + temp_mounth, '31-' + str(int(temp_mounth) - 1))
    else:
        last_folder = last_folder.replace(temp_day, str(int(temp_day) - 1))
    os.mkdir(last_folder)
    return last_folder


def print_lines(changed_files_name, name_lines):
    for i in range(max(len(changed_files_name), len(name_lines))):
        try:
            a = name_lines[i]
        except:
            a = 'None'
        try:
            b = changed_files_name[i]
        except:
            b = 'None'
        print(f'{a} - {b}')
        print('Не все фото загрузились')


def rename_files(contact_index, changed_files_name, name_lines, text_arr):
    last_folder = mypath
    this_photo, ex_photo = 9999, 0
    name_lines = name_lines[::-1]
    # rename
    for i in range(len(name_lines)):
        photo_number = 1
        ex_photo, this_photo = this_photo, int(name_lines[i][1].replace('_', ''))
        if this_photo > ex_photo:
            last_folder = create_new_folder(last_folder)
        while True:
            file_type = '.' + str(changed_files_name[i][-4:].replace('.', ''))
            if os.path.exists(last_folder + '\\' + name_lines[i][
                1] + f' {name_lines[i][0][contact_index:]} - {str(photo_number) + file_type}'):
                photo_number += 1
            else:
                shutil.move(mypath + '\\' + changed_files_name[i], last_folder + '\\' + name_lines[i][
                    1] + f' {name_lines[i][0][contact_index:]} - {str(photo_number) + file_type}')
                break
    if contact_index != 0:
        copy_address_text(text_arr)


def start_renaming(a, folder_dir, name_lines, text_arr):
    contact_index = {'park': 0, 'turan': 5, 'enb': 4, 'tbo': 4}

    # noinspection PyGlobalUndefined
    global mypath
    mypath = folder_dir
    print(mypath)
    # taking photo names from folder
    convert_all_files(get_files_name())
    changed_files_name = get_files_name()
    print("Photo count: ", len(changed_files_name), ' - ', len(name_lines))
    if len(changed_files_name) != len(name_lines):
        print_lines(changed_files_name, name_lines)
        while True:
            a = input('Press Enter to redownload')
            if a == 'Enter':
                return 1
            elif a == 'stop':
                return 0
    else:
        changed_files_name.sort(reverse=True)
        rename_files(contact_index[a], changed_files_name, name_lines, text_arr)
        return 0
