# 17.	Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint


def list_numb(x_):
    result = []
    for i in range(x_):
        result.append(randint(- x_, x_))
    return result


def Multipli_item_list(list, list_ind):
    multipli = 1
    for i in range(len(list_ind)):
        print({list[list_ind[i]]}, end=' ')
        multipli *= list[list_ind[i]]
    return multipli


numb = int(input('Введите целое положительное число: '))
multipli = list_numb(numb)
print(f'{multipli}')
list_ind = list(map(
    int,
    input('Введите позиции для произведения значений через пробел: ')
    .split()))
print(
    f'\nПроизведение последовательности = {Multipli_item_list(multipli,list_ind)}')
