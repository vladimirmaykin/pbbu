x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 and y1 == y2:
    print('Ход: НЕВОЗМОЖЕН')
else:
    if x1 == x2 or y1 == y2:
        print('Ход: ВОЗМОЖЕН')
    else:
        print('Ход: НЕВОЗМОЖЕН')