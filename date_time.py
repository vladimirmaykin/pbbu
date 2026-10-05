from datetime import datetime, date, time, timedelta

# d = date(2024,12,31)
# t = time(12,31,14)
#
# print(d, type(d))
# print(t, type(t))
# dt = datetime.combine(d, t)
# print(dt,type(dt))
#
# d = date.today()
# print(d)

# dt = datetime.now()
# print(dt)
#
# dt = datetime.now().replace(microsecond=0)
# print(dt.time())
# print(dt)

# dt = dt.replace(year=2020, month=10, day=30,hour=23,minute=59,second=59)
# print(dt)

# dtt = input('Ведите дату (дд.мм.гггг): ')
# datte = datetime.strptime(dtt, '%d.%m.%Y')
# print(datte)
# print(datte.strftime('%d.%m.%Y %X'))
# print(datte.strftime('%d.%m.%Y %H:%M'))
# print(datte.date())
# dt = datetime.now().replace(microsecond=0)
# dtt = dt.timetuple()
# print(dtt)
# for i in dtt:
#     print(i)
# dtt = dt.isocalendar()
# print(dtt)
# print(dt.weekday())
# print(dt.isoweekday())
# days = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
# print(days[dt.weekday()])

birthday = input('Введите дату рождения (дд.мм.гггг): ')

birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
dt_now = date.today()
year_ = dt_now.year
birthday = birthday.replace(year=year_)
print(birthday, dt_now, year_)

if birthday < dt_now:
    birthday = birthday.replace(year=year_ + 1)
res = birthday - dt_now
print(res)
if res.days == 0:
    print('Happy Birthday!')
else:
    print(f'До Вашего дня рождения {res.days} дн.')
