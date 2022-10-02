# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10


def get_bin_number(a: int):
    list_ = []
    while a >= 1:
        list_.append(a % 2)
        a = int(a / 2)
    list_.reverse()
    bin_number = ''
    for item in list_:
        bin_number += str(item)
    return int(bin_number)


num = int(input('Введите целое число: '))
print('bin ->',get_bin_number(num))