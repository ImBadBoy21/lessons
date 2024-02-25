import random

f_list = [random.randint(50, 80) for _ in range(10)]
s_list = [random.randint(30, 60) for _ in range(10)]

t_list = [('Выжил' if f_list[i] + s_list[i] < 100 else 'Погиб') for i in range(10)]

print('Урон первого отряда:', f_list)
print('Урон второго отряда:', s_list)
print('Состояние третьего отряда:', t_list)
