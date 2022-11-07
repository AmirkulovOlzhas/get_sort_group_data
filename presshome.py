counter = {"17 Мкр": 0,
           "Касирет": 0,
           "Алатау": 0,
           "Нурсат": 0,
           "Победа": 0
           }

for key, value in counter.items():
    print('+')
    counter[key]+=1
    temp_value = counter[key]

print(temp_value)
print(counter)