import random
rand_count = random.randint(5, 15)
left_round = random.randint(-1, rand_count)
right_round = random.randint(left_round, rand_count)
our_list = [x for x in range(rand_count + 1)]

print('Получили список до числа', rand_count,'и удалили элементы с индексами от', left_round, 'до', right_round)
print(our_list)
our_list[left_round:right_round+1] = []
print(our_list)

