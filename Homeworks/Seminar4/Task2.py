# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def select_not_repetitive(a: list):
    s_n_r_list = []
    for j in range(len(a)):
        for i in range(len(a)):
            if a[j] == a[i] and i != j:
                break
        else:
            s_n_r_list.append(a[j])
    if len(s_n_r_list) == 0:
        return 'В этом списке нет неповторяющихся элементов!'
    return s_n_r_list


list_ = list(map(int, input().split()))
print(list_)
print(f'Не повторяющиеся элементы из полученного списка: \
    {select_not_repetitive(list_)}')
