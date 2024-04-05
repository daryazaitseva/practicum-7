a = int(input('Введите число: '))
while a > 0:
    if int(a**0.5) * int(a**0.5) == a:
        print('Число является полным квадратом')
        break
    else:
        a = int(input('Введите число: '))
