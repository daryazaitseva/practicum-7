n = int(input('Введите число: '))
if n % 2 == 0:
    while n != 2:
        n = n / 2
        if n % 2 == 0:
            continue
        else:
            print('неверно')
            break
    if n == 2:
        print('верно')
else:
    print('неверно')
