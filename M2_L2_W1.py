count_list = [3, 7, 5]

while True:
    new_count = int(input('Новое число: '))
    if new_count == 9999:
        break
    else:
        count_list.append (new_count)
        print ('Текущий список чисел:', count_list)
        for i in count_list:
            print (i ** 2, i ** 3, i ** 4 )
        print()