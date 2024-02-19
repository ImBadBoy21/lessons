text = input('Введите строку: ')
text_list = list(text)
index = 0
i_count = 0

for sym in text_list:
    if sym == ':':
        text_list[index] = ';'
        i_count += 1
    index += 1

for i in text_list:
    print(i, end = '')
print('\nЗамен было выполнено: ', i_count)
