import time
import re


def take_name_data():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    book_r = []
    abc = "0123456789+:"
    for word in r:
        name = word.split('**')
        if len(name) > 1:
            data = name[len(name) - 1]
            while ':' in data:
                # сообщение11:5311:530:2211:530:0911:53
                if data[data.index(':') - 2] not in abc[:-2]:
                    data = data[data.index(':') + 3:]
                else:
                    break
            data = data[data.index(':') - 2:].replace('\n', '')
            book_r.append([name[0], data])
    return book_r


def check_data(nd):
    lines = []
    sum = 0
    for line in nd:
        line_1 = re.findall(r'\d{2}\:\d{2}', line[1])

        if '+' in line[1]:
            line_count = 3 + int(line[1][line[1].index('+') + 1:])
        else:
            line_count = len(line_1)
            if line_count > 4:
                print('+')
                line_count = 4
        print(f'{line[0]} - {line_1} - {line_count}')
        sum += line_count
        while line_count > 0:
            lines.append([line[0], line_1[0].replace(':', '_')])
            line_count -= 1
    print(f'количество имён фотографий = {sum}')
    return lines


def write_names_to_txt():
    name_data = take_name_data()
    return check_data(name_data)
