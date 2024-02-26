our_names = input('Введите Имя и Фамилию людей через запятые: ').split(', ')
our_ages = input('Введите их возраст через пробел: ').split(' ')
ages = [int(sym) for sym in our_ages]

for i in range(len(our_names)):
    message = 'Уважаемый(ая) {name}! Желаем Вам долгих лет жизни. С {age}-летием Вас. {name} мы Вас очень ценим'.format(
        name = our_names[i],
        age = ages[i]
    )
    print(message)