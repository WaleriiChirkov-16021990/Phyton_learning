# 1. Напишите программу, которая принимает на вход цифру,
#    обозначающую день недели, и проверяет, является ли этот день выходным.

#     *Пример:*

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
print('Для завершения press ctrl + C')
while True:
    try:
        num = int(input('Введите целое число от 1 до 7: '))
        if num < 1 or num > 7:
            raise ValueError
    except (Exception, ValueError):
        print('Получено число вне заданного диапазона!')
        continue

    if num > 5 and num < 8:
        print(f'{num} -> да')
    if num > 0 and num < 6:
        print(f'{num} -> нет')
