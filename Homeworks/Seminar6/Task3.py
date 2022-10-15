# было
# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#    второй и предпоследний и т.д.
#     *Пример:*
#
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]


# def multipli_item(a: list):
#     b = []
#     if len(a) % 2 != 0:
#         for i in range(int(len(a) / 2)):
#             b.append(a[i] * a[- 1 - i])
#         b.append(a[i + 1] ** 2)
#     if len(a) % 2 == 0:
#         for i in range(int(len(a) / 2)):
#             b.append(a[i] * a[- 1 - i])
#     return b


# list_ = [2, 3, 4, 5, 6]
# list_2 = [2, 3, 5, 6]
# print(multipli_item(list_))
# print(multipli_item(list_2))

# стало

def multipli_item(a: list):
    if len(a) % 2 != 0:
        return [a[i] * a[- 1 - i] if i <= int(len(a) / 2) \
                else (a[int(len(a)/2) + 1] ** 2) \
                for i in range(int(len(a) / 2) + 1)]
    return [a[- 1 - i] * a[i] for i in range(int(len(a) / 2))]


list_ = [2, 3, 8, 5, 6]
list_2 = [2, 3, 5, 6]
print(multipli_item(list_))
print(multipli_item(list_2))