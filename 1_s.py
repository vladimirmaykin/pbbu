g1 = int(input())
g2 = int(input())
g3 = int(input())

k_max = 0
g_max = max(g1, g2, g3)
if g1 == g_max: k_max = k_max + 1
if g2 == g_max: k_max = k_max + 1
if g3 == g_max: k_max = k_max + 1

print('Максимальная мощность:', g_max)
print('Количество лидеров:', k_max)