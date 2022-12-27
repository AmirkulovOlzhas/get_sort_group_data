import os
import sys
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


def rename_files(contact_index, changed_files_name, name_lines):
    i, temp_value = 0, 0
    this_photo, ex_photo = 9999, 0
    data_symbol = ''
    name_lines = name_lines[::-1]
    # rename
    for line in name_lines:
        temp_line = line.replace('\n', '').split(' ')
        temp_value = 1
        while True:
            ex_photo = this_photo
            this_photo = int(temp_line[1].replace('_', ''))
            if this_photo > ex_photo:
                data_symbol += 'l'
            try:
                file_type = '.' + str(changed_files_name[i][-4:].replace('.', ''))
                # надо изменить
                os.rename(mypath + '\\' + changed_files_name[i],
                          mypath + '\\' + data_symbol + temp_line[
                              1] + f' {temp_line[0][contact_index:]} - {str(temp_value) + file_type}')
                break
            except WindowsError:
                temp_value += 1
            except IndexError:
                print('.', end='')
                break
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno, e)
        i += 1
    copy_address_text()


def start_renaming(a, folder_dir, name_lines):
    contact_index = {'park': 0, 'abai': 5, 'enb': 4, 'tbo': 4}

    # noinspection PyGlobalUndefined
    global mypath
    mypath = folder_dir
    print(mypath)
    # taking photo names from folder
    all_files_name = get_files_name()
    print("Photo count: ", len(all_files_name))

    convert_all_files(all_files_name)
    changed_files_name = get_files_name()
    changed_files_name.sort(reverse=True)

    rename_files(contact_index[a], changed_files_name, name_lines)
