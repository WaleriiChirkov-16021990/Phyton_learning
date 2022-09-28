# 16.	Задайте список из n чисел последовательности (1+1/n) в степени n и выведите на экран их сумму.


from typing import List


def list_numb(x_):
    result = []
    for i in range(1, x_ + 1):
        result.append((1 + 1 / i) ** i)
    return result


def Sum_item_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


numb = int(input('Введите целое положительное число: '))
multipli = list_numb(numb)
print(f'Сумма последовательности = {round(Sum_item_list(multipli),3)}')
