# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

inpu_file = 'input_file.txt'
enco_file = 'rle_enco.txt'
deco_file = 'rle_deco.txt'


def rle_compression_str(data):
    encode_ = ''
    prev_ch = data[0]
    count = 1
    if not data:
        return ''
    for i in range(1, len(data)):
        if data[i] != prev_ch:
            encode_ += str(count) + prev_ch
            prev_ch = data[i]
            count = 1
        else:
            count += 1
            if count == 10:
                encode_ += str(count - 1) + prev_ch
                prev_ch = data[i]
                count = 1
    else:
        encode_ += str(count) + prev_ch
    return encode_


def rle_decompression_str(data):
    decode_ = ''
    count_ = ''
    for i in range(len(data)):
        if data[i].isdigit() and i % 2 == 0:
            count_ += data[i]
        else:
            decode_ += data[i] * int(count_)
            count_ = ''
    return decode_


def read_data_of_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        str_ = data.read()
        print(f'Файл {path} прочитан')
    return str_


def record_data_of_file(path, file):
    with open(path, 'w', encoding='utf-8') as data:
        data.write(f'{file}\n')
        print(f'Данные {file} успешно записаны в файл {path}')


def select_input():
    while True:
        try:
            select_input = int(input(\
                'Введите 1 для ввода данных, или 2 для чтения  из файла: '))
            if select_input == 1 or select_input == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print('Введите требуемое число для выбора.')
            continue
    if select_input == 1:
        str_ = input('Введите строку с многократным повторением символов: ')
    if select_input == 2:
        str_ = read_data_of_file(inpu_file)
    return str_


str_ = select_input()
print(f'Получены данные(строка): \t\t\t{str_}')
enco_str = rle_compression_str(str_)
print(f'Так выглядят сжатые данные \t\t\t{enco_str}')
str_deco = rle_decompression_str(enco_str)
print(f'Так выглядят данные после восстановления :\t{str_deco}')
record_data_of_file(deco_file, str_deco)
record_data_of_file(enco_file, enco_str)
if len(str_) <= len(enco_str):
    print('\nСжатие было бессмысленно, размер файла увеличился!')
