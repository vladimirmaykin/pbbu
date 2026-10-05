x = int(input())
y = int(input())

if x == 0 and y == 0: print('Положение: НАЧАЛО КООРДИНАТ')
else:
    if x != 0 and y == 0: print('Положение: ОСЬ X')
    else:
        if x == 0 and y != 0: print('Положение: ОСЬ Y')
        else:
            if x > 0 and y > 0: print('Положение: ПЕРВАЯ ЧЕТВЕРТЬ')
            else:
                if x < 0 and y > 0: print('Положение: ВТОРАЯ ЧЕТВЕРТЬ')
                else:
                    if x < 0 and y < 0: print('Положение: ТРЕТЬЯ ЧЕТВЕРТЬ')
                    else:
                        print('Положение: ЧЕТВЁРТАЯ ЧЕТВЕРТЬ')