print('Я помогу вам узнать ваш индекс массы тела и скажу пару слов')
height = float(input('Введите ваш рост: '))
weight = float(input('Введите вашу массу: '))
index = 0
coeff = 0
gender = input('Вы man or woman: ')
if gender == 'man':
    coeff = 94
elif gender == 'woman':
    coeff = 80
index = coeff * height / weight
