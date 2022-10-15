# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import os
from random import randint

col = 2021
max_ = 28
min_ = 1

print('\nПравила игры:')
print(f'На столе лежит {col} конфет(а). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_} конфет. Все конфеты оппонента достаются сделавшему последний ход.')


def out_red(text):
    return print('\033[31m {}'.format(text))


def out_yellow(text):
    return print('\033[33m {}'.format(text))


def out_blue(text):
    return print('\033[34m {}'.format(text))


def out_white(text):
    return print('\033[37m {}'.format(text))


def get_step_1_gam(tup: tuple):
    out_yellow(f'Всего конфет : {tup[1]}')
    gamer_1 = 0
    while True:
        try:
            if tup[4] == 2:
                gamer_1 = int(input('Игрок 1 сделайте ход :'))
            if tup[4] == 1:
                gamer_1 = int(input('Ваш ход :'))
            if tup[3] <= gamer_1 <= tup[2] and gamer_1 <= tup[1]:
                break
            else:
                raise ValueError
        except ValueError:
            print('Вы ввели недопустимое число. Повторите ввод!')
            continue
    col = tup[1] - gamer_1
    motion = tup[5] + 1
    if tup[4] == 1:
        opponent_ = 3
    else:
        opponent_ = 2
    return opponent_, col, max_, min_, tup[4], motion, gamer_1


def get_step_2_gam(tup: tuple):
    out_blue(f'Всего конфет : {tup[1]}')
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
    motion = tup[5] + 1
    return 1, col, max_, min_, tup[4], motion, gamer_2


def get_step_bot(tup: tuple):
    out_red(f'Всего конфет : {tup[1]}')
    up_lim = tup[2]
    lo_lim = tup[3]
    if tup[1] % (tup[2] + tup[3]) != 0:
        up_lim = lo_lim = tup[1] % (tup[2] + tup[3])
        bot_mition = randint(lo_lim, up_lim)
    else:
        bot_mition = (tup[3] + tup[2]) - tup[6]
    print(f'Бот загребает {bot_mition} конфет(у) =(')
    col = tup[1] - bot_mition
    motion = tup[5] + 1
    return 1, col, max_, min_, tup[4], motion, bot_mition


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
            if tup[4] == 2:
                return get_step_2_gam(tup)
            if tup[4] == 1:
                return get_step_bot(tup)


def start(col: int, max: int, min: int, mode_: int):
    clea_ = lambda: os.system('cls')
    while True:
        try:
            if mode_ == 2:
                gamer_ = int(input(\
                    'Введите номер игрока 1 или 2, который начнет игру: '))
            else:
                gamer_ = int(input(\
                    'Введите номер, для игрока 1 или для бота 2, кто начнет игру: '))
            if gamer_ == 1 or gamer_ == 2:
                break
            else:
                raise ValueError
        except ValueError:
            clea_()
            print('Вы ввели недопустимое число. Потворите ввод!\n')
            continue
    if mode_ == 2:
        if gamer_ == 1:
            print('Начинает 1-й игрок.')
        else:
            print('Начинает 2-й игрок.')
    if mode_ == 1:
        if gamer_ == 1:
            print('Начинаете вы.')
        else:
            print('Начинает бот.')
    motion = 1
    opponent_move = 0
    return gamer_, col, max, min, mode_, motion, opponent_move


def select_mode():
    clea_ = lambda: os.system('cls')
    while True:
        try:

            mode_ = int(input('\nКакой режим игры предпочитаете? \
                Введите 1 для игры с ботом, или 2 для игры с другим игроком: '))
            if mode_ == 1 or mode_ == 2:
                if mode_ == 2:
                    print('Вы выбрали режим игры с игроком!')
                    break
                else:
                    print('Вы выбрали режим игры с ботом!')
                    break
            else:
                raise ValueError
        except ValueError:
            clea_()
            print('Вы ввели недопустимое число. Потворите ввод!\n')
            continue
    return mode_


def game(col: int, max: int, min: int):
    mode_ = select_mode()
    tup = start(col, max, min, mode_)
    while get_result(tup):
        tup = next_step(tup)
    out_white('\nИгра завершена')
    vin_ = ''
    if tup[0] == 1:
        gamers = 'Игрок 1'
    elif tup[0] == 2:
        gamers = 'Игрок 2'
    else:
        gamers = 'бот'
        vin_ = 'Поздравляю, вы выйграли у компьютера!'
    print(f'{vin_}\nПроиграл {gamers}!')


game(col, max_, min_)
