def f_voler():
    print('\nНаш вольер:')
    for i in range(1, len(animals) + 1):
        print('В', i, 'клетке сидит:', animals[i - 1])

cells = int(input('Сколько клеток в зоопарке? '))
animals = []

for i in range(1, cells + 1):
    print('Кто сидит в', i,'клетке', end=' ')
    animal = input()
    animals.append(animal)

f_voler()

new_animal = input('\nСегодная к нам привезли новое животное, кто это? ')
num_cell = int(input('В какую клетку посадить животное? '))
animals.insert(num_cell - 1, new_animal)

f_voler()

old_animal = input('\nСегодня забрали животное. Кого забрали? ')
animals.remove(old_animal)

f_voler()