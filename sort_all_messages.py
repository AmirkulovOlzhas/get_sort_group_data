import time


def take_name_data():
    r = open('stuf/all_messages.txt', 'r', encoding='utf8')
    book_r = []
    abc = "0123456789+:"
    for word in r:
        name = word.split('**')
        if len(name) > 1:
            data = name[len(name) - 1]
            for letter in data:
                if letter not in abc:
                    data = data.replace(letter, '')
            book_r.append([name[0], data])
    return book_r


def check_data(nd):
    sum = 0
    mes_name = open('stuf/mes_contact_names.txt', 'w', encoding='utf8')
    lines = ''
    for line in nd:
        # print(line[1])
        line_count = line[1].count(":")
        # если на линий  2 ':' но второй элемент не ':' это значит что на линий виедо
        # а видео могут дублировать линию
        if line_count > 1:
            if '+' in line[1]:
                line_1 = line[1][:line[1].index('+')]
            else:
                line_1 = line[1]
            print(line_1)
            s=0
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
        sum += int(line_count)

        while line_count > 0:
            if line[1]:

                if line[1].count(':') == 1:
                    dot_index = line[1].index(':')
                    line[1] = line[1][dot_index - 2:dot_index + 3]

                elif line[1].count(':') > 1:
                    # # мб проблема тут видео сохранются в mes_contact_names по два раза
                    # print(line[1], ' 2 ":"')
                    dot_index = line[1].index(':')
                    line[1] = line[1][dot_index + 3:]
                    dot_index = line[1].index(':')
                    line[1] = line[1][dot_index - 2:dot_index + 3]
                if ':' in line[1]:
                    lines += line[0] + ' ' + line[1].replace(":", "_") + '\n'
            line_count -= 1
    mes_name.write(lines[:-1])
    print(sum)


def write_names_to_txt():
    name_data = take_name_data()
    check_data(name_data)
    time.sleep(2)
