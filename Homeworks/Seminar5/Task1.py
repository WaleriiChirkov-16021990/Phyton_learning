# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def delete_word_args(lis, item):
    return [x for x in lis if x.count(item) == 0]


st = input('Введите текст, который содержит слово(а) с "абв": ').split()
print(' '.join(delete_word_args(st, 'абв')))
