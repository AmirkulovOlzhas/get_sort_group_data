import os
import re
import sys
import shutil
from os import listdir
from os.path import isfile, join
from folder_works import copy_address_text
from config import contact_dict


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
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


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


def rename_files(changed_files_name, name_lines, text_arr, group_number):
    name_lines = name_lines[::-1]
    n = 1
    if group_number == 0:
        n = 0
    # rename
    folder_date = ''
    for i in range(len(name_lines)):
        contact_name = name_lines[i][0]
        if '-' in contact_name:
            contact_name = contact_name.split('-')[n]
        photo_number = 1
        temp_date = re.findall(r'\d{4}\-\d{2}\-\d{2}', changed_files_name[i])[0]
        temp_date = temp_date[-2:] + '-' + temp_date[5:7] + '-' + temp_date[:4]
        if temp_date != folder_date:
            temp_fn = folder_date = temp_date
            folder_num = ''
            while True:
                folder = os.path.join("D:\\WA_photo\\", temp_fn + contact_dict[group_number] + folder_num)
                if os.path.exists(folder):
                    folder_num += '-'
                else:
                    os.mkdir(folder)
                    break
        while True:
            file_type = '.' + str(changed_files_name[i][-4:].replace('.', ''))
            if os.path.exists(folder + '\\' + name_lines[i][1]
                              + f' {contact_name} - {str(photo_number) + file_type}'):
                photo_number += 1
            else:
                a = name_lines[i][1] + f' {contact_name} - {str(photo_number) + file_type}'
                shutil.move(mypath + '\\' + changed_files_name[i], folder + '\\' + a)
                break

    copy_address_text(text_arr)


def start_renaming(folder_dir, name_lines, text_arr, group_number):
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
            temp = input('Press Enter to redownload')
            if temp == 'Enter':
                return 1
            elif temp == 'stop':
                return 0
    else:
        changed_files_name.sort(reverse=True)
        rename_files(changed_files_name, name_lines, text_arr, group_number)
        return 0
