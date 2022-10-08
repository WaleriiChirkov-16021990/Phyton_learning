# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def get_easy_multipli_list(n: int):
    easy_m = []
    i = 2
    while n > 1 and i <= n:
        if n % i == 0:
            easy_m.append(i)
            n /= i
        else:
            i += 1
    return easy_m


nums = int(input('Введите натуральное число: '))
print(f'Список простых множителей: {get_easy_multipli_list(nums)} ')
