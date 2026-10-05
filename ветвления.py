
color = input('Цвет светофора')
match color:
    case 'red'| 'no':
        print('STOP')
    case 'green': print('GO')
    case 'yellow': print('Ready')
    case _:
        print('Цвет', color)

# h = float(input('Введите время суток'))
# if h >= 4 and h <= 12:
#     print('Morning')
# elif h >=12 and h < 17:
#     print('Day')
# elif h >= 17 and h < 24:
#     print('Evening')
# elif (h >= 0 and h < 4 or h == 24):
#     print('Night')
# else:
#     print('Время введено неверно!')





# a = 26
# b = 36
# c = a > b
# print(c)

# if a > b:
#     print('A > B')
#     print('A больше B')
# elif a < b:
#     print('A < B')
# else:
#     print('A = B')
# print('END')

# if a > b:
#     print('A > B')
#     print('A больше B')
# else:
#     if a < b:
#         print('A < B')
#     else:
#         print('A = B')