while True:
    try:
        N = int(input('Введите N: '))
        if 1<=N<=1000: break
        print('1≤N≤1000 !')
    except:
        print('Неверный ввод!')

словарь = {k[0]:' '.join(k[1:]) for k in [input(f'Введите {i+1}-ю запись: ').split() for i in range(N)]}

while True:
    try:
        M = int(input('Введите M: '))
        if 1<=M<=100: break
        print('1≤M≤100 !')
    except:
        print('Неверный ввод!')

слова = [input(f'Введите {i+1}-е слово: ') for i in range(M)]

[print(f'{i}:', словарь. setdefault(i,'Нет в словаре')) for i in слова]