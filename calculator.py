print('Я помогу вам узнать ваш индекс массы тела и скажу пару слов')
height = float(input('Введите ваш рост: '))
weight = float(input('Введите вашу массу: '))
index = 0
coeff = 0
if index < 18.5:
    print('Деффицит массы')
elif (index < 30) and (index > 25):
    print('избыток массы')
elif index > 30:
    print('ожирение, чтобы узнать степень обратитесь к диетологу')
else:
    print('норма')
