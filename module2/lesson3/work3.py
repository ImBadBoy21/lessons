dog_numbers = [15, 20, 14, 30, 12]
maximum = dog_numbers[0]
minimum = dog_numbers[0]
i_max = 0
i_min = 0
index = 0

for i in dog_numbers:
    if maximum < i:
        maximum = i
        i_max = index
    if minimum > i:
        minimum = i
        i_min = index
    index += 1

print('Макс:', maximum,'его индекс', i_max, 'Мин:', minimum, 'его индекс', i_min)
print(dog_numbers)
dog_numbers[i_max] = minimum
dog_numbers[i_min] = maximum
print(dog_numbers)
