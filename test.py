def take_name_data():
    r = open('stuf/text.txt', 'r', encoding='utf8')
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
    mes_name = open('stuf/park_mes_name.txt', 'w', encoding='utf8')
    lines = ''
    for line in nd:
        line_count = line[1].count(":")
        if '+' in line[1]:
            line_count += int(line[1][line[1].index('+') + 1:])
        print(line, '- ', line_count)
        sum += int(line_count)

        while line_count > 0:
            lines += line[0]+'\n'
            line_count -= 1
    mes_name.write(lines[:-1])
    print(sum)


def start_park_rename():
    name_data = take_name_data()
    check_data(name_data)
