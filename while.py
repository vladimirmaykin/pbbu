
n = int(input('>'))

nn = n
sm = 0
cnt = 0
while n > 0:
    rem = n % 10
    sm = sm + rem
    cnt += 1
    n = n // 10

print(f'В чмсле "{nn}" {cnt} цифр суммой {sm}')


# n = int(input('>'))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1
#     #print(n)
#     n = int(input('>'))
#
# print(f'Сумма - {sm}\n'
#       f'Кол-во - {cnt}')

# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     #if i == 7: continue
#     if i == 17:
#         break
#     print(i, end=' ')
# else:
#     print('\nOK')


# print()
# i = 0
# while i < 10:
#     print(i, end=' ')
#     i += 1 # i = i + 1
