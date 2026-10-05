l1 = int(input())
l2 = int(input())
l3 = int(input())

flag = 1
if l1 + l2 > l3 and l1 + l3 > l2 and l1 + l3 > l2 and l2 + l3 > l1:
    flag = 0
if flag == 1:
    print('Тип: ТРЕУГОЛЬНИК НЕ СУЩЕСТВУЕТ')
else:
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Тип: РАВНОСТОРОННИЙ')
    else:
        if l1 == l2 or l1 == l3  or l2 == l3:
            print('Тип: РАВНОБЕДРЕННЫЙ')
        else:
            print('Тип: РАЗНОСТОРОННИЙ')