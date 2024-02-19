numbers = []

count_numbers = int(input('Введите количество чисел в списке: '))

for i in range(count_numbers):
    print('Введите', i + 1, 'число:', end = ' ')
    num = int(input())
    numbers.append(num)

divider = int(input('Введите делитель: '))

index = 0
i_sum = 0
for i in numbers:
    a = i % divider
    if a == 0:
        print('Индекс числа', i, ':', index)
        i_sum += index
    index += 1

print('Сумма индексов:',i_sum)