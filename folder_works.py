import os
import sys
from datetime import date
from os import listdir

import patoolib

global parent_dir
global ext_dir
# noinspection PyRedeclaration
parent_dir = r"D:\\Wa_photo\\"
# noinspection PyRedeclaration
ext_dir = ''


def create_folder(ct):
    if ct == 'park':
        folder_flag = 'P'
    elif ct == 'enb':
        folder_flag = '-'
    else:
        folder_flag = ''

    today = date.today()
    folder_name = str(today.day) + '-' + str(today.month) + '-' + str(today.year) + folder_flag

    path = os.path.join(parent_dir, folder_name)
    folder_number = 0
    while True:
        try:
            if folder_number != 0:
                path += str(folder_number)
            os.mkdir(path)
            break
        except:
            folder_number += 1

    print('folder created')
    print(folder_name)
    print('path: ', path)
    return path


def extract_rar(rar_file, extract_dir):
    if rar_file[-4:] == '.zip':
        patoolib.extract_archive(r'D:\\WA_photo\\downloads\\' + rar_file, outdir=extract_dir)
        global ext_dir
        ext_dir = extract_dir
        print('rar file extracted')
        delete_rar(rar_file)
        return extract_dir


def delete_rar(rar_file):
    os.remove(r'D:\\WA_photo\\downloads\\' + rar_file)


def start_folder_work(ct):
    return extract_rar(listdir(r'D:\\WA_photo\\downloads\\')[0], create_folder(ct))


def copy_address_text():
    try:
        print(ext_dir)
        with open('stuf/sorted_messages_list.txt', 'rb') as src, \
                open(ext_dir + r'\\0Address.txt', 'wb') as dst:
            dst.write(
                src.read())
    except Exception as e:
        print('no address file')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
