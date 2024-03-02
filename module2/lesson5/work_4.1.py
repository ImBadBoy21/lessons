def create(sym):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    s_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if alphabet.count(sym):
        new_sym = alphabet[(alphabet.index(sym)+shift) % 33]
        return new_sym
    elif s_alphabet.count(sym):
        new_sym = s_alphabet[(s_alphabet.index(sym) + shift) % 33]
        return new_sym
    else:
        return sym

text = input('Введите ваш текст: ')
shift = int(input('Введите сдвиг: '))
new_text = [create(x) for x in text]
print("".join(new_text))
