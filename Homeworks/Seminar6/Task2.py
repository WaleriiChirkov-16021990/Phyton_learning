# было

# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     *Пример:*
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# def select_not_even_index(a):
#     not_even = []
#     if len(a) >= 2:
#         for i in range(1, len(a), 2):
#             not_even.append(a[i])
#         return not_even
#     else:
#         print('В списке всего одно значение! ')


# def get_sum_item_list(a):
#     sum_ = 0
#     for i in a:
#         sum_ += i
#     return sum_


# list_ = [2, 3, 5, 9, 3]
# print(f' На нечётных позициях элементы {select_not_even_index(list_)}')
# print(f' Сумма нечётных элементов: {get_sum_item_list(select_not_even_index(list_))}')

# стало


def get_sum_not_even_index(a):
    if len(a) == 1:
        print('В списке всего одно значение! Возвращаю сам список. ')
        return a
    else:
        return sum([a[i] for i in range(1, len(a), 2) if len(a) >= 2])


list_ = [2, 3, 5, 9, 3]
print(f'Сумма нечётных элементов: {get_sum_not_even_index(list_)}')


def f(x):
    if x > 10:
        return True
    else:
        return False