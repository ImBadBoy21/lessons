left_round = int(input('Левая граница: '))
right_round = int(input('Правая граница: '))

first_list = [x ** 3 for x in range(left_round, right_round + 1)]
second_list = [x ** 2 for x in range(left_round, right_round + 1)]

print('Список кубов чисел в диапазоне от', left_round, 'до', right_round, ':', first_list)
print('Список кваратов чисел в диапазоне от', left_round, 'до', right_round, ':', second_list)