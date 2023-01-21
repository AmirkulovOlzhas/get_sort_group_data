import re


def take_name_data(smt):
    name_data = []
    abc = "0123456789:"
    for word in smt:
        name = word[0].replace('**', '')
        if '+' in word[-1]:
            data = word[-4:]
        else:
            data = []
            for i in word:
                if len(i) == 5:
                    if all(num in abc for num in i):
                        data.append(i)
            if len(data) > 4:
                data = data[len(data) - 4:]

        name_data.append([name, data])
    return name_data


def check_data(name_data):
    file_names = []
    sum = 0

    for line in name_data:
        if '+' in line[1][-1]:
            line_count = 3 + int(line[1][-1].replace('+', ''))
        else:
            line_count = len(line[1])
        sum += line_count
        photo_date = re.findall(r'\d{2}\:\d{2}', ''.join(line[1]))[0]
        while line_count > 0:
            file_names.append([line[0], photo_date.replace(':', '_')])
            line_count -= 1
    print(f'----------------------количество имён фотографий = {sum}----------------------')
    return file_names


def write_names_to_txt(smt):
    name_data = take_name_data(smt)
    return check_data(name_data)
