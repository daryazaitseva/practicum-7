n = int(input('Введите число: '))
while n != 2 and n % 2 == 0:
    n = n / 2
if n == 2:
    print('верно')
if n % 2 != 0:
    print('неверно')
