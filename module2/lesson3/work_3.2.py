
def count_sym(text_1,text_2):
    check_sym_1 = 0
    check_sym_2 = 0
    for i in text_1:
        if i == '!':
            check_sym_1 += 1
    for i in text_2:
        if i == '?':
            check_sym_2 += 1
    if check_sym_1 > check_sym_2:
        new_text = text_1 + ' ' + text_2
    elif check_sym_1 < check_sym_2:
        new_text = text_2 + ' ' + text_1
    else:
        new_text = 'Ой'
    return new_text

first_mess = input('Первое сообщение: ')
second_mess = input('Второе сообщение: ')
print('Третье сообщение:', count_sym(first_mess, second_mess))