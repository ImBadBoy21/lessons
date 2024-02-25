our_list = [input('Введите слово: ') for _ in range(3)]
text = input('Введите текст: ')

check_list = [[our_list[i], text.count(our_list[i])] for i in range(3)]
print('Вывод:', check_list)
