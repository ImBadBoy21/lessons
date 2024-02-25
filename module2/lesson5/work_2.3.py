def check():
    work = True
    while work:
        print('Число: ', end=' ')
        num = int(input())
        if 0 <= num < 255:
            work = False
        else:
            print('Неправильное число! Введите снова')
    return num

text = 'Ваш IP-адресс {0}.{1}.{2}.{3}'.format(
    check(),
    check(),
    check(),
    check()
)

print(text)
