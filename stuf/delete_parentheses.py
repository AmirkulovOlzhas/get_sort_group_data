import os
from os import listdir
from os.path import isfile, join


def rename_file(this_line, pr, outside):
    if pr == 1:
        temp_line_name = this_line.replace(' (', '-')
        temp_line_name = temp_line_name.replace(')', '')
    else:
        temp_line_name = this_line
    print(this_line, ' - ', temp_line_name)
    if not outside:
        os.rename(mypath + '\\' + this_line, mypath + '\\' + '00' + temp_line_name[29:])
    else:
        os.rename(mypath + '\\' + this_line, mypath + '\\' + temp_line_name)


def rename_all_files(all_files_name, outside=False):
    for line in all_files_name:
        p = 0
        if ('(' in line) & (')' in line):
            p = 1
        rename_file(line, p, outside)


mypath = r"C:\Users\OFFICE\Desktop\test"
files_name = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# if need to rename enb abay
rename_all_files(files_name)
