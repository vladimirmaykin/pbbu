# список - упорядоченный набор объектов
import copy

# num = [22,33,44,55,99]
# print(num[0])
# print(num[2])
# print(num[1:-2])
# print(num[:])
# print(num[::2])
# print(num[2:])
# print(num[2::-1])
#print(num[::-1])


# num = [1,2,[42,4]]
#nn = num
#nn = num[:]
#nn = num.copy()
# nn = copy.deepcopy(num)
#
# num[1] =  3333
# num[-1][1] = 400
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)

num = [22,100,44,100,99]
print(num)
num.append(100) # ДОБАВИТЬ В КОНЕЦ
print(num)
num.insert(0,300) # добавить в начало
print(num)
num.append([1,2])   # ДОБАВИТЬ В КОНЕЦ
num.extend([1,2])

#num +=[1,2]
num = num + [1,2]
print(num)

n = num.pop()
nn = num.pop(0)
print(nn, num, n)

# while 100 in num:
#     num.remove(100)
# print(nn, num, n)
print(num.index(100))
print(num.count(100))
# num.clear()
# print(num)


num = [22,33,44,55,99, 11]

for i in range(len(num)):
    print(i, num[i], end=' ')
print()

# cnt = 0
# for i in num:
#     print(cnt, i, end=' ')
#     cnt = cnt + 1
# print()

for i in enumerate(num):
    #print(i, end=' ')
    print(i[0], i[1], end=' ')
print()

#   кортеж - упорядоченный набор неизменяемых объектов
tp = (22,33,44,99)
#k = 7,
# K = 7,
# print(K[0], K, type(K))
k, *i, z = 7,5,9,10,1,32,56,100
print(k, *i, z)

names = ['Dasha', 'Masha', 'Sasha', 'Gasha','Andrusha']
# names.reverse()
# names.sort(reverse=True)
names.sort()
for k, i in enumerate(names):
    print(f'{k}, {i}')
for i in zip(names, num):
    print(k,i)

arr = [0] * 10
#print(arr)
for i in range(len(arr)):
    arr[i] = i + 1
print(arr)

ls = []
for i in range(10):
    ls.append(i + 1)
print(ls)

#   кортеж - упорядоченный набор неизменяемых объектов
tp = (22,33,44,99)

k, i, *z = 7,5,9,10,1,32,56,100
print(k, i, z)

tp = ('login','password')
print(tp, id(tp))
buf = list(tp)
buf[-1] = 'new_password'
tp = tuple(buf)
print(tp, id(tp))

# левый циклический сдвиг
l = [22,33,44,55,99]
temp = l[0]
n = len(l)
for i in range(n - 1):
    l[i] = l[i + 1]
l[-1] = temp
print(l)
# temp = l.pop(0)
# l.append(temp)
# print(l)
x = 10
y = 15
print(x, y)
z = x
x = y
y = z
print(x, y)

x, y = y, x
print(x, y)

print(5 if len(l) < 7 else 125)
ls = [i + 1 for i in range(10) if i > 4]
print(ls)

names = ('Dasha', 'Masha', 'Sasha', 'Gasha','Andrusha')
age = (22,33,44,55,11)

for r, (n,a) in enumerate(zip(names, age), 1):
     print(f'{r}, {n} - {a}')



