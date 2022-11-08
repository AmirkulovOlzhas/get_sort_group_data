import os
from os import listdir
from os.path import isfile, join


def rename_file(this_line):
    temp_line_name = this_line.replace(' (', '-')
    temp_line_name = temp_line_name.replace(')', '')
    os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)


mypath = r"C:\Users\OFFICE\Desktop\8112022-"
all_files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for line in all_files_name:
    if ('(' in line) & (')' in line):
        rename_file(line)
