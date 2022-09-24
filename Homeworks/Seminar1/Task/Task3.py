# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#     *Пример:*

#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

print('Для завершения press ctrl + C \n')

while True:
    try:
        x_coordinate = int(input('Введите координату точки Х: '))
        y_coordinate = int(input('Введите координату точки У: '))
        if x_coordinate == 0 or y_coordinate == 0:
            raise ValueError
    except (Exception, ValueError):
        print('Несоответствие задаче! Необходимы целые числа с условием X ≠ 0 и Y ≠ 0')
        continue
    if x_coordinate > 0:
        if y_coordinate > 0:
            print(f'x = {x_coordinate}; y = {y_coordinate} -> 1')
        else:
            print(f'x = {x_coordinate}; y = {y_coordinate} -> 4')
    else:
        if y_coordinate > 0:
            print(f'x = {x_coordinate}; y = {y_coordinate} -> 2')
        else:
            print(f'x = {x_coordinate}; y = {y_coordinate} -> 3')
    print('Продолжим: ')
