# 4. Напишите программу, которая по заданному номеру четверти,
#    показывает диапазон возможных координат точек в этой четверти (x и y).

print('Для завершения press ctrl + C\n')
while True:
    try:
        num = int(input('Введите целое число от 1 до 4: '))
        if num < 1 or num > 4:
            raise ValueError
    except (Exception, ValueError):
        print('Получено число вне требуемого диапазона!')
        continue

    if num == 1:
        print('Диапазон координаты Х > 0; Y > 0.')
    elif num == 2:
        print('Диапазон координаты Х < 0; Y > 0.')
    elif num == 3:
        print('Диапазон координаты Х < 0; Y < 0.')
    else:
        print('Диапазон координаты Х > 0; Y < 0.')
