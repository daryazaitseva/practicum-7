n = int(input('Введите объем последнего кубика: '))
v = 0
for i in range(1, int(n ** (1 / 3)) + 1):
    v = i**3
    if v <= n:
        print(v, end=' ')