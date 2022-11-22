import os
from os import listdir
from os.path import isfile, join


def rename_file(this_line, pr, outside):
    if pr == 1:
        temp_line_name = this_line.replace(' (', '-')
        temp_line_name = temp_line_name.replace(')', '')
    else:
        temp_line_name = this_line
    if not outside:
        os.rename(mypath + '\\' + this_line, mypath + '\\' + '00' + temp_line_name[29:])
    else:
        os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)


def rename_all_files(afn, outside=False):
    for this_line in afn:
        p = 0
        if ('(' in this_line) & (')' in this_line):
            p = 1
        rename_file(this_line, p, outside)


def start_renaming(a, folder_name):
    # a = input("park, abai, enb :")
    if a == 'park':
        contact = 0
    elif a == 'abai':
        contact = 5
    else:
        contact = 4

    # mypath = r"C:\Users\OFFICE\Desktop\test"

    # noinspection PyGlobalUndefined
    global mypath
    mypath = folder_name

    # taking photo names from folder
    all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print("len", len(all_files_name))

    rename_all_files(all_files_name, outside=True)
    # taking updated photo names from folder
    all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    i, temp_value = 0, 0

    # rename
    with open('stuf/mes_contact_names.txt', 'r', encoding='utf8') as f:
        this_photo, ex_photo = 1, 0
        data_symbol = ''
        for line in f:
            temp_line = line.replace('\n', '').split(' ')
            temp_value = 1
            while True:
                ex_photo = this_photo
                this_photo = int(temp_line[1].replace('_', ''))
                if this_photo < ex_photo:
                    data_symbol += 'l'
                try:
                    file_type = '.' + str(all_files_name[i][-4:].replace('.', ''))
                    os.rename(mypath + '\\' + all_files_name[i],
                              mypath + '\\' + data_symbol + temp_line[
                                  1] + f' {temp_line[0][contact:]} - {str(temp_value) + file_type}')
                    break
                except Exception as e:
                    print('tsm-57: ', e)
                    temp_value += 1
            i += 1
