t = int(input())

if t < -20: print('Режим: ЭКСТРЕМАЛЬНЫЙ ХОЛОД')
if t >= -20 and t < 0: print('Режим: ХОЛОДНО')
if t >= 0 and t < 20: print('Режим: ПРОХЛАДНО')
if t >= 20 and t < 30: print('Режим: КОМФОРТНО')
if t >= 30: print('Режим: ЖАРКО')
