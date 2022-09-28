# 18.	Реализуйте алгоритм перемешивания списка.


from random import randint


def mixing_list(list_):
    result = []
    for i in range(len(list_)):
        temp = randint(0, len(list_) - 1)
        result.append(list_[temp])
        del list_[temp]
    return result


list = [1, 2, 3, 4, 5, 6, 7]
mix_ = mixing_list(list)
print(mix_)
