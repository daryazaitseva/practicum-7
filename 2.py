str = input('Введите строку: ')
str_1 = []
for i in range(2, len(str) + 1, 3):
    str_1.append(str[i])
print(*str_1)
