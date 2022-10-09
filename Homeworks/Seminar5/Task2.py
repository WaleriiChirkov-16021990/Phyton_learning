# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import os

col = 31
max_ = 28
min_ = 1

print(f'На столе лежит {col} конфет(а). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_} конфет. Все конфеты оппонента достаются сделавшему последний ход.')


def get_step_1_gam(tup: tuple):
    print(f'Всего конфет : {tup[1]}')
    gamer_1 = 0
    while True:
        try:
            gamer_1 = int(input('Игрок 1 сделайте ход :'))
            if tup[3] <= gamer_1 <= tup[2] and gamer_1 <= tup[1]:
                break
            else:
                raise ValueError
        except ValueError:
            print('Вы ввели недопустимое число. Повторите ввод!')
            continue
    col = tup[1] - gamer_1
    return 2, col, max_, min_


def get_step_2_gam(tup: tuple):
    print(f'Всего конфет : {tup[1]}')
    gamer_2 = 0
    while True:
        try:
            gamer_2 = int(input('Игрок 2 сделайте ход :'))
            if tup[3] <= gamer_2 <= tup[2] and gamer_2 <= tup[1]:
                break
            else:
                raise ValueError
        except ValueError:
            print('Вы ввели недопустимое число. Повторите ввод!')
            continue
    col = tup[1] - gamer_2
    return 1, col, max_, min_


def get_result(tup: tuple):
    if tup[1] == 0:
        return False
    else:
        return True


def next_step(tup: tuple):
    if get_result(tup):
        if tup[0] == 1:
            return get_step_1_gam(tup)
        else:
            return get_step_2_gam(tup)


def start(col, max, min):
    clea_ = lambda: os.system('cls')
    while True:
        try:
            gamer_ = int(input(\
                'Введите номер игрока 1 или 2, который начнет игру: '))
            if gamer_ == 1 or gamer_ == 2:
                break
            else:
                raise ValueError
        except ValueError:
            clea_()
            print('Вы ввели недопустимое число. Потворите ввод!\n')
            continue
    if gamer_ == 1:
        print('Начинает 1-й игрок.')
    else:
        print('Начинает 2-й игрок.')
    return gamer_, col, max, min


def game(col: int, max: int, min: int):
    start_ = start(col, max, min)
    tup = next_step(start_)
    while get_result(tup):
        tup = next_step(tup)
    print('\nИгра завершена')
    print(f'Проиграл игрок {tup[0]}')


game(col, max_, min_)
