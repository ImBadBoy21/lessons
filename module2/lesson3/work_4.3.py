goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]



print('Текущий ассортимент:', goods)
print()

count_goods = int(input('Сколько фруктов вы хотите добавить? '))

for i in range(count_goods):
    new_good = []
    good = input('Название фрукта: ')
    price = int(input('Цена: '))
    new_good.append(good)
    new_good.append(price)
    goods.append(new_good)

for elem in goods:
    elem[1] = round(elem[1] * 1.08,2)


print('Новый ассортимент', goods)

