left_round = int(input('Левая граница: '))
right_round = int(input('Правая граница: '))

first_list = [x for x in range(left_round, right_round + 1) if x % 2 != 0]


print('Список нечетных чисел в диапазоне от', left_round, 'до', right_round, ':', first_list)
