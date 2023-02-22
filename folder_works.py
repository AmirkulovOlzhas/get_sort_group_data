import os, sys
import re
import shutil
import time
import patoolib
from datetime import date
from os import listdir
from config import contact_dict

global parent_dir
# global ext_dir
# noinspection PyRedeclaration
parent_dir = r"D:\\Wa_photo\\"
# noinspection PyRedeclaration
# ext_dir = ''


def create_folder(ct):
    today = date.today()
    if isinstance(ct, int):
        temp_cd = contact_dict[ct]
    else:
        temp_cd = ct
    folder_name = str(today.month) + '-' + str(today.day) + '-' + str(today.year) + temp_cd + '!'

    path = os.path.join(parent_dir, folder_name)
    folder_number = 0
    while True:
        try:
            os.mkdir(path)
            time.sleep(3)
            break
        except:
            folder_number += 1
            path += str(folder_number)
            print(path)
    print('----------------------folder created----------------------')
    return [path, temp_cd]


def extract_rar(rar_files, ct):
    for file in rar_files:
        if file[-4:] == '.zip':
            extract_dir = create_folder(ct)
            patoolib.extract_archive(r'D:\\WA_photo\\downloads\\' + file, outdir=extract_dir[0])
            print('----------------------rar file extracted----------------------')
            delete_rar(file)
            return extract_dir
    if file[-4:] in ['jpeg', '.mp4']:
        extract_dir = create_folder(ct)
        shutil.move(r'D:\\WA_photo\\downloads\\'+rar_files[0], extract_dir[0])
        return extract_dir


def delete_rar(rar_file):
    os.remove(r'D:\\WA_photo\\downloads\\' + rar_file)


def copy_address_text(text_mes_arr, ext_dir):
    try:
        text_arr = list(filter(None, text_mes_arr))
        with open(ext_dir + r'\\0Address.txt', 'w', encoding='utf8') as dst:
            for text in text_arr:
                dst.write(text)
    except Exception as e:
        print('no address file')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def start_folder_work(ct):
    print('Фотографий загружаются...')
    i = 0
    while True:
        if len(listdir(r'D:\\WA_photo\\downloads\\')) > 0:
            return extract_rar(listdir(r'D:\\WA_photo\\downloads\\'), ct)
        else:
            time.sleep(1.5)
            i += 1
            print(end='.')
            if i % 10 == 0:
                print()

