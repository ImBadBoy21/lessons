

workers = int(input('Введите кол-во сотрудников: '))
s_workers = []

for i in range(1, workers + 1):
    print('Зарплата', i,'сотрудника:', end=' ')
    salary = int(input())
    s_workers.append(salary)

for i in range(len(s_workers)-1,-1,-1):
    print('Проверяю элемент', s_workers[i],'под номером', i)
    if s_workers[i] == 0:
        s_workers.pop(i)

print(s_workers)