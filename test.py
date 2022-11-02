def take_name_data():
    r = open('text.txt', 'r', encoding='utf8')
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
    for line in nd:
        line_count = line[1].count(":")
        if '+' in line[1]:
            line_count += int(line[1][line[1].index('+')+1:])
        print(line, '- ', line_count)
        sum += int(line_count)
    print(sum)


# if input("Download? 1-yes everything else - no: ") == 'yes':
name_data = take_name_data()
check_data(name_data)
# else:
#     print('puck')
