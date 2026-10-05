s = 'Здравствуйте, гости!'

# print(s[0])
# print(s[6])
# print(s[-1])
# print(len(s))
# print(s[::1])
# print(s[:12])
# print(s[::-1])
# for i in s:
#     print(i, end=' ')
# print(s[19])
# for i in range(len(s)):
#     print(s[i], end=' ')

print(s.index(','))
print(s.isalpha())
print(s.isnumeric())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.startswith('З'))
print(s.endswith('!'))

print(n := s.lower())
print(n)

print(s.capitalize())
print(s.title())
print(s.rjust(40))
print(s.ljust(40))
print(s.center(40))
print(s.strip())    # удаляем пробелы по краям
print(s.strip('!З '))
print(s.index('т', 8, 12))
print(s.find('т', 8, 11))
print(s.replace('т', 'LN').replace(',',''))

ls = s.split()  # создает список
ls = s.split(', ')  # создает список
print(ls)

js = ', '.join(ls)
print(js)


