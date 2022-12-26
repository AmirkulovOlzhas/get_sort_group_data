import time


def take_name_data():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    book_r = []
    abc = "0123456789+:"
    for word in r:
        name = word.split('**')
        if len(name) > 1:
            data = name[len(name) - 1]
            while ':' in data:
                if data[data.index(':') - 2] not in abc[:-2]:
                    data = data[data.index(':') + 3:]
                else:
                    break
            data = data[data.index(':') - 2:].replace('\n', '')
            book_r.append([name[0], data])
    return book_r


def check_data(nd):
    mes_name = open('stuf/mes_contact_names.txt', 'w', encoding='utf8')
    lines = []
    print('cam25: ', len(nd))
    for line in nd:
        line_count = line[1].count(":")
        s = 0
        if line_count > 1:
            if '+' in line[1]:
                line_1 = line[1][:line[1].index('+')]
            else:
                line_1 = line[1]
            for i in range(line_count):
                if ':' not in line_1:
                    break
                if line_1.index(':') != 2:
                    line_1 = line_1[((i + 1) * 5) + 4:]
                    s += 1
                else:
                    line_1 = line_1[(i + 1) * 5:]
        line_count -= s

        if '+' in line[1]:
            line_count += int(line[1][line[1].index('+') + 1:])

        while line_count > 0:
            if line[1]:
                dot_index = line[1].index(':')
                line[1] = line[1][dot_index - 2:dot_index + 3]

                if ':' in line[1]:
                    temp = line[0] + ' ' + line[1].replace(":", "_")
                    lines.append(temp)
            line_count -= 1
    return lines


def write_names_to_txt():
    name_data = take_name_data()
    return check_data(name_data)