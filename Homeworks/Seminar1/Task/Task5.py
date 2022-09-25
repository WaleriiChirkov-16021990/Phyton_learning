# 5. Напишите программу, которая принимает на вход координаты
#    двух точек и находит расстояние между ними в 2D пространстве.

#     *Пример:*

#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
from unittest import result


print('Для завершения press ctrl + C \n')


def LengthLine2D(x1, y1, x2, y2):
    result = sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2)
    return result


while True:
    try:
        x1_coordinate = int(input('Введите координату точки Х: '))
        y1_coordinate = int(input('Введите координату точки У: '))
        x2_coordinate = int(input('Введите координату точки Х: '))
        y2_coordinate = int(input('Введите координату точки У: '))
    except (Exception, ValueError):
        print('Несоответствие задаче! Необходимы целые числа!')
        continue
    length_line = LengthLine2D(
        x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate)
    print(f'A({x1_coordinate},{y1_coordinate});B({x2_coordinate},{y2_coordinate}) -> {round(length_line,3)}')
