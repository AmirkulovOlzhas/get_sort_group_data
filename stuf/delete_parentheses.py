import os
from os import listdir
from os.path import isfile, join


def rename_file(this_line, pr):
    if pr == 0:
        temp_line_name = this_line.replace(' (', '-')
        temp_line_name = temp_line_name.replace(')', '')
    else:
        temp_line_name = this_line
    os.rename(mypath + '\\' + this_line, mypath + '\\' + '00' + temp_line_name[29:])


def rename_all_files(all_files_name):
    for line in all_files_name:
        p = 0
        if ('(' in line) & (')' in line):
            p = 1
        rename_file(line, p)


mypath = r"C:\Users\OFFICE\Desktop\test"
files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]
