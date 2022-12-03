a = '0:18'
b = "09:18"
c = a + b
print(a)
print(b)
# c[:2].replace(':', '_')
dot_index = c.index(':')
c = c[dot_index+3:]
print(c)