pr = int(input())
dist = int(input())
mas = int(input())
fast = int(input())

base = 0
add = 0
summ = 0

if pr >= 5000:
    base = 0
    if mas > 20: add = add + 500
    if fast == 1: add = add + 300
    summ = summ + base + add
else:
    if dist <= 5: base = base + 200
    else:
        if dist <= 20: base = base + 400
        else: base = base + 700
    if mas > 20: add = add + 500
    if fast == 1: add = add + 300
    summ = summ + base + add

print('Базовая стоимость:', str(base))
print('Доплата:', str(add))
print('Итого:', str(summ))