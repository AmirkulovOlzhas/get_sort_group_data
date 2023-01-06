import os
import sys
import time
import patoolib
from datetime import date
from os import listdir

global parent_dir
global ext_dir
# noinspection PyRedeclaration
parent_dir = r"D:\\Wa_photo\\"
# noinspection PyRedeclaration
ext_dir = ''


def create_folder(ct):
    contact_dict = {'park': 'P', 'enb': '-', 'abai': '', 'tbo': 'T'}
    today = date.today()
    folder_name = str(today.day) + '-' + str(today.month) + '-' + str(today.year) + contact_dict[ct]

    path = os.path.join(parent_dir, folder_name)
    folder_number = 0
    time.sleep(3)
    while True:
        try:
            os.mkdir(path)
            break
        except:
            folder_number += 1
            path += str(folder_number)

    print('----------------------folder created----------------------')
    return path


def extract_rar(rar_file, extract_dir):
    if rar_file[-4:] == '.zip':
        patoolib.extract_archive(r'D:\\WA_photo\\downloads\\' + rar_file, outdir=extract_dir)
        global ext_dir
        ext_dir = extract_dir
        print('----------------------rar file extracted----------------------')
        delete_rar(rar_file)
        return extract_dir


def delete_rar(rar_file):
    os.remove(r'D:\\WA_photo\\downloads\\' + rar_file)


def copy_address_text(text_mes_arr):
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
    return extract_rar(listdir(r'D:\\WA_photo\\downloads\\')[0], create_folder(ct))
