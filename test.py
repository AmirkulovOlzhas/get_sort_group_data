import os
import sys
import shutil
from os import listdir
from os.path import isfile, join
from folder_works import copy_address_text


def get_files_name():
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]


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
