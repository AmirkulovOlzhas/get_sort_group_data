def take_name_data():
    r = open('text.txt', 'r', encoding='utf8')
    book_r = []
    abc = "0123456789+:"
    for word in r:
        name = word.split('**')
        data = name[len(name) - 1]
        for letter in data:
            if letter not in abc:
                data = data.replace(letter, '')
        book_r.append([name[0], data])
    return book_r


def check_data(nd):
    sum = 0
    for line in nd:
        line_count = line[1].count(":")-1
        line_sum = 1
        if line_count > 1:
            if '+' in line[1]:
                if '*' in line[1]:
                    line_sum += int(line[1].split('+')[1])
        line_sum += line_count
        print(line, ': ',  line_sum)
        sum += int(line_sum)
    print(sum)


if input("Download? 1-yes everything else - no: ") == 'yes':
    name_data = take_name_data()
    check_data(name_data)
else:
    print('puck')
