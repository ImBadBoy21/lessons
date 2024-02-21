count_player = int(input('Количество участников: '))
count_team = int(input('Количество участников в одной команде: '))
our_teams = []
def my_def(players, team):
    num = 1
    print('Количество выполнений цикла', players // team)
    for i in range(players // team):
        our_teams.append(list(range(num, num + team)))
        num += team

check = True
while check:
    if count_player % count_team != 0:
        print(count_player,'участников невозможно поделить на команды по', count_team,'человек')
        count_team = int(input('Введите другое число участников в одной команде: '))
    elif count_player % count_team == 0:
        my_def(count_player,count_team)
        print(our_teams)
        break
    else:
        print('Неправильный ввод!')
        break