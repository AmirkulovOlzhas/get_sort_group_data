# def combos(l, l_index):
#     print('--------- ---------', l_index, '----------- ----------')
#     temp_l = l.copy()
#     for i in range(l_index, len(l)):
#         print(temp_l[i - 1], temp_l[i])
#         temp_l[i - 1], temp_l[i] = temp_l[i], temp_l[i - 1]
#         print(temp_l)
#     l_index -= 1
#
#     if l_index > 0:
#         combos(l, l_index)


def combos1(l, l_index):
    temp_l = l.copy()
    tll = l_index
    while tll != len(l):
        temp_l[l_index - 1], temp_l[tll] = temp_l[tll], temp_l[l_index - 1]
        print(temp_l)
        tll += 1
    l_index -= 1

    if l_index > 0:
        print('--------- ---------', l_index, '----------- ----------')
        combos1(l, l_index)


l = [6, 5, 4, 3, 2, 1]
print(l)
combos1(l, len(l) - 1)
