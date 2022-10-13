# Создайте программу для игры в ""Крестики-нолики"".


def get_game_board(num: int):
    return [x for x in range(1, num * num + 1)]


def draft_board(lis: list):
    print('------------')
    for i in range(3):
        print(f'| {lis[0 + i * 3]} | {lis[1 + i *3]} | {lis[2 + i * 3]} |')
        print('------------')


def get_input(game_board, player):
    flag = False
    while not flag:
        try:
            player_input = int(input(f'Сделайте ход {player} : '))
        except:
            print('Некорректный ввод. Введите свободное число')
            continue
        if player_input >= 1 and player_input <= 9:
            if (str(game_board[player_input - 1]) not in 'XO'):
                game_board[player_input - 1] = player
                flag = True
            else:
                print('Клетка уже занята')
        else:
            print('Не корректный ввод, введите число от 1 до 9 .')


def check_board(board: list):
    vin_cod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))
    for item in vin_cod:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False


def start_game():
    count_ = 0
    flag = False
    game_board = get_game_board(3)
    while not flag:
        draft_board(game_board)
        if count_ % 2 == 0:
            char = 'X'
        else:
            char = 'O'
        get_input(game_board, char)
        count_ += 1
        if count_ >= 5:
            temp = check_board(game_board)
            if temp:
                print(f'\nИгрок , который играл за "{temp}"  выйграл\n')
                flag = True
                break
        if count_ == 9:
            print('Ходы закончиились.Ничья!')
            break
    draft_board(game_board)


start_game()
