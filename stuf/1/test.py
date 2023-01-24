import os.path

import numpy as np
import re
from os import listdir
from os.path import isfile, join
import shutil


def dict_test():
    abc = "0123456789+:"
    word = 'abc**Пересланное сообщение11:5311:530:2211:55'
    # word = 'abc**Пересланное сообщение11:5411:5411:54+3'
    name = word.split('**')
    data = []
    if len(name) > 1:
        data = name[len(name) - 1]
        while ':' in data:
            # сообщение11:5311:530:2211:530:0911:53
            if data[data.index(':') - 2] not in abc[:-2]:
                data = data[data.index(':') + 3:]
                print('-')
            else:
                print('+')
                break
        data = data[data.index(':') - 2:].replace('\n', '')
        print([name[0], data])

    # Абай-Бегара**Пересланное сообщение11:5411:5411:54+3
    k = [['aaa', '11:2211:2211:22'],
         ['aab', '11:2211:2211:2'],
         ['abb', '11:2211:211:2'],
         ['ab1b', '11:221:2211:2'],
         ['bb1b', '11:21:2211:2']

         ]
    for d in k:
        print('------------------------------------------------')
        line = d
        print(line[1])
        line_count = line[1].count(":")
        result = len(line[1].replace(':', '')) / 4
        print(f'line count = {line_count}  -  result  =  {result}')
        if line_count > 1:
            print('--')
            if '+' in line[1]:
                line_1 = line[1][:line[1].index('+')]
                print(f'+ {line_1}')
                result = 3
            else:
                s = 0
                line_1 = line[1]
                print(line_1)
                for i in range(line_count):
                    if ':' not in line_1:
                        print('break')
                        break
                    if line_1.index(':') != 2:
                        print('if: ', line_1)
                        line_1 = line_1[5 + 4:]
                        # s += 1
                    else:
                        print('else:', line_1)
                        line_1 = line_1[5:]
                result -= s
        print('result: ', int(result))


def array_test():
    y = []
    for i in range(10):
        x = np.array([i, i + 1])
        y.append(x)
    y = np.asarray(y)
    print(y)


def re_func():
    k = [['aaa', '11:2211:2211:22'],
         ['aab', '11:2211:2211:2'],
         ['abb', '11:2211:211:2'],
         ['ab1b', '11:221:2211:2'],
         ['bb1b', '11:21:2211:2'],
         ['сообщение', '11:5311:530:2211:530:0911:5311:53']]

    lines = []
    for line in k:
        line_1 = re.findall('\d{2}\:\d{2}', line[1])

        if '+' in line[1]:
            line_count = 3 + int(line[1][line[1].index('+') + 1:])
        else:
            line_count = len(line_1)
            if line_count > 4:
                print('+')
                line_count = 4
        print(f'{line[0]} - {line_1} - {line_count}')
        while line_count > 0:
            lines.append(line[0] + ' ' + line_1[0].replace(':', '_'))
            line_count -= 1
    return lines

    b = re.findall(r'\_77\d{9}', a)
    print(b)
    print(type(b[-1]))
    print(b[-1][1:])


# a = 'album-false_120363029944605916@g.us_AA6DAF357E8F58393A234AD720370594_77785497042@c.us-false_120363029944605916\
#     @g.us_C61C5517878245921104B2FEC18F4D60_77785497042@c.us-8'
# re_func(a)


def re_func2(line):
    photo_date = re.findall(r'.{2}\:.{2}', ''.join(line))[0]
    print(photo_date)
    # print(photo_date.replace(':', '_'))


# re_func2(['0:19', '11:44', '11:44', '+11'])

def folders_for_photo():
    mypath = "D:\WA_photo\downloads\WhatsApp Unknown 2023-01-23 at 13.04.24"
    x = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(x)
    folder_date = ''
    folders_path = "D:\WA_photo\downloads"
    for i in range(len(x)):
        temp_date = re.findall(r'\d{4}\-\d{2}\-\d{2}', x[i])[0]
        if temp_date != folder_date:
            folder_date = temp_date
            temp_fn = folder_date
            if not os.path.exists(folders_path + '\\' + temp_fn):
                os.mkdir(folders_path + '\\' + temp_fn)
        shutil.move(mypath + '\\' + x[i], folders_path + '\\' + temp_fn)


folders_for_photo()
