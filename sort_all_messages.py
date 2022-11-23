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
    every_second = 0
    for line in nd:
        line_count = line[1].count(":")
        if '+' in line[1]:
            line_count += int(line[1][line[1].index('+') + 1:])
        print(line, '- ', line_count)
        sum += int(line_count)

        while line_count > 0:
            if line[1]:
                if line[1][2] == ':':
                    line[1] = line[1][:5]
                else:
                    dot_index = line[1].index(':')
                    line[1] = line[1][dot_index - 2:dot_index + 3]
            # if line[1] empty :
            try:
                lines += line[0] + ' ' + line[1].replace(":", "_") + '\n'
            except:
                if every_second == 0:
                    lines += line[0] + ' ' + 'Video' + '\n'
                    every_second += 1
                else:
                    every_second = 0
            line_count -= 1
    mes_name.write(lines[:-1])
    print(sum)


def write_names_to_txt():
    name_data = take_name_data()
    check_data(name_data)
