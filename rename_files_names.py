import os
from os import listdir
from os.path import isfile, join
from folder_works import copy_address_text


def rename_file(this_line, outside):
    try:
        temp_line_name = this_line.replace(' (', '')
        temp_line_name = temp_line_name.replace(')', '')
        # если в файле видео, то он оказывается внизу, этот иф меняет слова из за чего при сортировке все меняется
        if temp_line_name[-4:] == '.mp4':
            temp_line_name = temp_line_name.replace('Video', 'Image')
            print(temp_line_name)
        else:
            temp_line_name = temp_line_name
        if not outside:
            os.rename(mypath + '\\' + this_line, mypath + '\\' + '00' + temp_line_name[29:])
        else:
            os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)
    except Exception as e:
        print(e)


def rename_all_files(afn, outside=False):
    for this_line in afn:
        rename_file(this_line, outside)


def start_renaming(a, folder_name):
    # a = input("park, abai, enb :")
    if a == 'park':
        contact = 0
    elif a == 'abai':
        contact = 5
    else:
        contact = 4

    # noinspection PyGlobalUndefined
    global mypath
    mypath = folder_name

    # taking photo names from folder
    all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print("len", len(all_files_name))

    rename_all_files(all_files_name, outside=True)
    # taking updated photo names from folder
    changed_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    i, temp_value = 0, 0
    # сортируем по убыванию
    changed_files_name.sort()
    print(changed_files_name)

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
                    file_type = '.' + str(changed_files_name[i][-4:].replace('.', ''))
                    os.rename(mypath + '\\' + changed_files_name[i],
                              mypath + '\\' + data_symbol + temp_line[
                                  1] + f' {temp_line[0][contact:]} - {str(temp_value) + file_type}')
                    break
                except WindowsError:
                    temp_value += 1
                except Exception as e:
                    print(e)
            i += 1
    copy_address_text()
