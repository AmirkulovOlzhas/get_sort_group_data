# import numpy as np
#
# vac_nums = [0, 0, 0, 0, 0,
#             1, 1, 1, 1, 1, 1, 1, 1,
#             2, 2, 2, 2,
#             3, 3, 3
#             ]
# mean = sum(vac_nums) / len(vac_nums)
# variance = sum(list(map(lambda x: (x - mean) ** 2, vac_nums))) / (len(vac_nums))
# print(variance)
#
# a = np.array(vac_nums)
# mean1 = np.sum(a) / a.size
# v = np.sum((a - mean1) ** 2) / a.size
# print(v)



# players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
# m = sum(players) / len(players)
# deviations = [(x - m) ** 2 for x in players]
# variance = (sum(deviations) / len(players)) ** (1 / 2)
# print('---', variance)
# v = (sum(list(map(lambda x: (m - x) ** 2, players))) / (len(players)))**(1/2)
# result = list(filter(lambda x: abs(x - m) <= int(v), players))
# print(m, ' - ', int(v), '\n', result)

#
# a = []
# al = 'DEFGHIJKLMNOPQRSTUVWXYZ'
# alb = ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH']
# for i in range(len(al)):
#     a.append(f'{al[i]}11:{al[i]}40')
# for i in range(len(alb)):
#     a.append(f'{alb[i]}11:{alb[i]}40')
# print(a)

import msvcrt, time
i = 0
while True:
    i = i + 1
    if msvcrt.kbhit():
        print(msvcrt.getwche())
        if msvcrt.getwche() == 'a':
            break
    time.sleep(0.1)
print(i)