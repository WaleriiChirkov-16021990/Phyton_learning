# Задана натуральная степень k. Сформировать случайным образом список коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint


def get_polynomial_list(k):
    polynomial_ = \
         [repr(randint(1, 100)) + 'x' + '^' + repr(i) for i in range(k, 1, -1)]
    polynomial_.append(repr(randint(1, 100)) + 'x')
    polynomial_.append(repr(randint(1, 100)))
    for i in range(len(polynomial_)):
        if polynomial_[i][0] == '1' and polynomial_[i][1] == 'x' \
             and len(polynomial_[i]) > 1:
            polynomial_[i] = polynomial_[i][1:]
        if polynomial_[i][0] == '0':
            polynomial_[i] = '0'
    polynomial_final = []
    for i in polynomial_:
        if i != '0':
            polynomial_final.append(i)
    return polynomial_final


def record_polynomal_str(k: list):
    polynomial = " + ".join(k)
    polynomial += ' = 0'
    return polynomial


k = int(input("Введите натуральную степень: "))
polylist_ = get_polynomial_list(k)
poly_str = record_polynomal_str(polylist_)

with open('polynomial.txt', 'w', encoding='UTF-8') as data:
    data.write(f'{poly_str}\n')

print(f'В файл polynomial.txt записали многочлен счетени {k}: {poly_str}')
