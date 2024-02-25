
def add_film(d_film):
    if your_films.count(d_film):
        print('Этот фильм уже есть в вашем списке.')
    else:
        your_films.append(d_film)

def paste_film(d_film):
    if your_films.count(d_film):
        print('Этот фильм уже есть в вашем списке.')
    else:
        check_id = input('После какого фильма вставить этот фильм? ')
        check_film = 0
        for i in your_films:
            if i == check_id:
                i_film = your_films.index(i) + 1
                your_films.insert(i_film, d_film)
                check_film += 1
        if check_film == 0:
            print('Такого фильма нет в вашем топе фильмов.')
            paste_film(new_film)

def delete_film(d_film):
    if your_films.count(d_film):
        your_films.remove(d_film)
    else:
        print('Этого фильма итак нет в вашем топе фильмов.')

def check_command(d_film, command):
    if command == 'добавить':
        add_film(d_film)
    elif command == 'вставить':
        paste_film(d_film)
    elif command == 'удалить':
        delete_film(d_film)
    else:
        print('Неправильно введена команда')
        print('Команды: добавить, вставить, удалить')
        new_command = input('Введите команду: ')
        check_command(new_film, new_command)


your_films = []

work = True
while work:
    print('Ваш текущий топ фильмов:', your_films)
    new_film = input('Название фильма: ')
    print('Команды: добавить, вставить, удалить, выход')
    command = input('Введите команду: ')
    if command == 'выход':
        work = False
    else:
        check_command(new_film, command)
    print()


