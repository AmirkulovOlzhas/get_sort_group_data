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
    for line in nd:
        line_count = line[1].count(":")
        if line_count > 1:
            if '+' in line[1]:
                print(line)


name_data = take_name_data()
check_data(name_data)
