s = {}
while True:
    try:
        n = int(input("Кількість працівників: "))
        for j in range(1,n+1):
            d = []
            for i in range(1):
                d = dict(Прізвище=input('Введіть прізвище: '),Вік =int(input('Введіть вік: ')),Освіта = input('Введіть освіту: '),Посада= (input('Введіть посаду: ')))
            s[j] = d
        for i in s:
            if s[i].get('Вік') > 30 and s[i].get('Освіта') != 'Вища':
                print(s[i])
    except:ValueError
    print('Введено невірне значення ,введіть заново: ')