pack = []
decode = []
bad_pack = 0

pack_mat = int(input('Введите количество пакетов: '))

for i_pack in range(pack_mat):
    print('\nПакет номер', i_pack + 1, ':')
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Слишком много ошибок!')
        bad_pack += 1
    pack = []

print('\nПолученно сообщение', decode)
print('Количество ошибок в сообщении', decode.count(-1))
print('Количество потерянных сообщений', bad_pack)
