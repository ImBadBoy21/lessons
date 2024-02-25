prices = [1.09, 23.56, 57.84, 4.56, 6.78]

f_percent = int(input('Повышение на первый год: '))
f_percent = round(1 + f_percent/100, 2)

s_percent = int(input('Повышение на второй год: '))
s_percent = round(1 + s_percent/100, 2)

f_price = [round(x * f_percent, 2) for x in prices]
s_price = [round(x * s_percent, 2) for x in f_price]

print('Сумма цен за каждый год:', round(sum(prices), 2), round(sum(f_price), 2), round(sum(s_price), 2))
