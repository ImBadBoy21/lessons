him_name = input('Введите имя: ')
him_debt = int(input('Введите долг: '))
message = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(
    him_name,
    him_debt
)
print(message)