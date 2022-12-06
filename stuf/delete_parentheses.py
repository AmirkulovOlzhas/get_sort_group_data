a = '10:5910:0610:5910:59+3'
b = a[:a.index('+')]
print(b)
s=0
for i in range(4):
    if ':' not in b:
        break
    if b.index(':') != 2:
        b = b[((i+1) * 5) + 4:]
        print('+ ', b)
        s+=1
    else:
        b = b[(i+1) * 5:]
        print('- ', b)
print(s)