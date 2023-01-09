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
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def convert_all_files(afn):
    # to correct sort list
    for this_line in afn:
        rename_file(this_line)


def rename_files(contact_index, changed_files_name, name_lines, text_arr):
    second_folder = mypath
    i = 0
    this_photo, ex_photo = 9999, 0
    name_lines = name_lines[::-1]
    # rename
    for line in name_lines:
        temp_line = line.replace('\n', '').split(' ')
        photo_number = 1
        ex_photo = this_photo
        this_photo = int(temp_line[1].replace('_', ''))
        if this_photo > ex_photo:
            second_folder += 'l'
            os.mkdir(second_folder)
        while True:
            file_type = '.' + str(changed_files_name[i][-4:].replace('.', ''))
            if os.path.exists(second_folder + '\\' + temp_line[
                1] + f' {temp_line[0][contact_index:]} - {str(photo_number) + file_type}'):
                photo_number += 1
            else:
                shutil.move(mypath + '\\' + changed_files_name[i], second_folder + '\\' + temp_line[
                    1] + f' {temp_line[0][contact_index:]} - {str(photo_number) + file_type}')
                break
        i += 1
    copy_address_text(text_arr)


def start_renaming(a, folder_dir, name_lines, text_arr):
    contact_index = {'park': 0, 'abai': 5, 'enb': 4, 'tbo': 4}

    # noinspection PyGlobalUndefined
    global mypath
    mypath = folder_dir
    print(mypath)
    # taking photo names from folder
    all_files_name = get_files_name()
    print("Photo count: ", len(all_files_name), ' - ', len(name_lines))
    if len(all_files_name) != len(name_lines):
        print('Не все фото загрузились')
        return 1
    else:
        convert_all_files(all_files_name)
        changed_files_name = get_files_name()
        changed_files_name.sort(reverse=True)
        rename_files(contact_index[a], changed_files_name, name_lines, text_arr)
        return 0
