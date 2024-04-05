n, k, r = map(int, input('Введите длину нити в первый день, '
                         'процент и необходимую длину: ').split(' '))
count = 1
while n < r:
    n = n * (100 + k)/ 100
    count += 1
print(count)