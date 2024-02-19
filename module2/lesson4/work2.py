new_string = input('Введите строку: ')
sym = int(input('Введите номер символа: '))
string_list = list(new_string)
our_sym = string_list[sym - 1]

check_left = False
check_right = False
left_sym = ''
right_sym = ''

if sym > 1:
    left_sym = string_list[sym - 2]
    print('Символ слева:', left_sym)
    check_left = True
else:
    print('Слева символов нет')
if sym < len(string_list) - 1:
    right_sym = string_list[sym]
    print('Символ справа', right_sym)
    check_right = True
else:
    print('Справа символов нет')
count = 0
if string_list[sym-1] == left_sym and check_left:
    count += 1
if string_list[sym-1] == right_sym and check_right:
    count += 1
if count != 0:
    if count == 1:
        print('Есть ровно один такой же символ')
    else:
        print('Есть два таких же символа')
else:
    print('Таких же символов нет')
