import numpy as np
import re

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
        x = np.array([i, i+1])
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
        line_1 = re.findall(r'\d{2}\:\d{2}', line[1])

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


print(re_func())
