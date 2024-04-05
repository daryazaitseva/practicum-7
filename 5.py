n = int(input('Введите объем последнего кубика: '))
v = 0
for i in range(1, 100001):
    v = i**3
    if v <= n:
        print(v, end=' ')
