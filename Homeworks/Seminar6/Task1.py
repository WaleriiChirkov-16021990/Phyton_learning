# Напишите программу, удаляющую из текста все слова, содержащие ""{input}"".

# было


# def delete_word_args(lis, item):
#     return [x for x in lis if x.count(item) == 0]

# input_ = input('Введите текст который будем искать для удаления: ')
# st = input(f'Введите текст, который содержит минимум 1 слово с \
#     "{input_}": ').split()
# print(' '.join(delete_word_args(st, input_)))


# стало


def delete_word_args(lis, item):
    return list(filter(lambda x: not x.count(item), lis))

input_ = input('Введите текст который будем искать для удаления: ')
st = input(f'Введите текст, который содержит минимум 1 слово с \
    "{input_}": ').split()
print(' '.join(delete_word_args(st, input_)))
