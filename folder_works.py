import os
from datetime import date
from os import listdir

import patoolib

global parent_dir

# noinspection PyRedeclaration
parent_dir = r"D:\\Wa_photo\\"


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
    os.mkdir(path)
    print('folder created')
    return folder_name


def extract_rar(rar_file, extract_dir):
    patoolib.extract_archive(r'D:\\WA_photo\\downloads\\' + rar_file, outdir=extract_dir)
    print('rar file extracted')
    # delete archive
    return extract_dir


def start_folder_work(ct):
    return extract_rar(listdir(r'D:\\WA_photo\\downloads\\')[0], parent_dir + create_folder(ct))
