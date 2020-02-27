s_1 = list(input('Введіть символи: '))
s = list()
count = 0
if s_1[0] == '!':
    print('Перший символ знак оклику')
elif "!" not in s_1:
    print('В послідовності немає знаків оклику')
else:
    for i in range(len(s_1)):
        s += s_1[i]
        if '!' not in s and s_1[i] == ' ':
            count += 1
    print('У послідовності',count,'пробілів до першого знаку оклику' )
print(s_1)