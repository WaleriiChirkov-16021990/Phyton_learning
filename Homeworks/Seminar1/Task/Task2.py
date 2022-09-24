# 2. Напишите программу для. проверки истинности утверждения
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print('Проверим истинность указанного утверждения: ¬(X ⋁ Y ⋁ Z) = ¬ X ⋀ ¬ Y ⋀ ¬ Z')
X = True
Y = False
Z = True


def True_or_False(X, Y, Z):
    left_Value = not (X or Y or Z)
    right_Value = not X and not Y and not Z
    if left_Value == right_Value:
        return True
    else:
        return False


print('теоретическая проверка показала что: ')
if True_or_False:
    print('Утверждение истинно для всех значений предикат!')
else:
    print("Утверждение ложно !")
print('Проверим это на практике!')
print("Введите значения 1 или 0 для 3-х переменных в разных комбинациях\n")
while True:
    XYZ = ['X', 'Y', 'Z']
    input_num = []
    for i in range(3):
        input_num.append(int(input(f'Введите значение {XYZ[i]}: ')))
    print(
        f'¬({input_num[0]}  ⋁  {input_num[1]}  ⋁  {input_num[2]}) = ¬ {input_num[0]} ⋀ ¬ {input_num[1]} ⋀ ¬ {input_num[2]}')
    print(True_or_False(input_num[0], input_num[1], input_num[2]))
