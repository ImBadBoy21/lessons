our_text = input('Введите строку: ')
sym = input('Введите дополнительную строку: ')

first_list = [x * 2 for x in our_text]
second_list = [x + sym for x in first_list]

print('Список удвоенных символов:', first_list)
print('Склейка с дополнительным символом:', second_list)