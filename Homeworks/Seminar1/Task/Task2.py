# 2. Напишите программу для. проверки истинности утверждения
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print('Проверим истинность указанного утверждения: ¬(X ⋁ Y ⋁ Z) = ¬ X ⋀ ¬ Y ⋀ ¬ Z')


def out_red(text):
    print('\033[31m {}'.format(text))


def out_blue(text):
    print('\033[34m {}'.format(text))


def out_green(text):
    print('\033[32m {}'.format(text))


def out_white(text):
    print('\033[39m {}'.format(text))


def True_or_False():
    res = True
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                left_Value = not (X or Y or Z)
                right_Value = not X and not Y and not Z
                if left_Value != right_Value:
                    out_red(f'X = {X}, Y = {Y}, Z = {Z}')
                    out_red(False)
                    res = False
                else:
                    out_green(f'X = {X}, Y = {Y}, Z = {Z}')
                    out_blue(True)
    return res


print('теоретическая проверка показала что: ')
result = True_or_False()
if result:
    print('Утверждение истинно для всех значений предикат!')
else:
    out_red("Утверждение ложно !")
out_white('Убедимся в этом на практике!')
print("Введите значения 1 или 0 для 3-х переменных в разных комбинациях\n")
while True:
    XYZ = ['X', 'Y', 'Z']
    input_num = []
    for i in range(3):
        input_num.append(int(input(f'Введите значение {XYZ[i]}: ')))
    print(
        f'¬({input_num[0]}  ⋁  {input_num[1]}  ⋁  {input_num[2]}) = ¬ {input_num[0]} ⋀ ¬ {input_num[1]} ⋀ ¬ {input_num[2]}\n')
