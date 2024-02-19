person_ID = []

count_person = int(input('Сколько сотрудников в компании? '))
for i in range(1, count_person + 1):
    print('Введите ID', i,'сотрудника')
    new_ID = int(input())
    person_ID.append(new_ID)
print('Список ID', person_ID)
search_ID = int(input('Какой ID ищем? '))

if search_ID in person_ID:
    print("Worker on work")
else:
    print('Worker is not work')
