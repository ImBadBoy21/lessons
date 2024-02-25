name = input('Ваше имя: ')
order_number = int(input('Номер заказа: '))

message = 'Здравствуйте, {our_name}! Ваш номер заказа: {our_num}. Приятного дня!'.format(
    our_name = name,
    our_num = order_number
)

print(message)