# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


from re import I


l = [1, 5, 2, 3, 4, 6, 1, 7]


def get_max_list(l, max):
    if len(l) == 1:
        return l[0]

    for i in range(max, len(l)):
        if l[i] > max:
            max = l[i]

    if len(l) > 1:


        return get_max_list

# def get_up2(nums):
#     for i in range(len(nums)):
#         nums1 = nums[i:]
#         for j in range(len(nums1)):
#             ups = [nums1[0]]
#             for x in nums1:
#                 if x > max(ups):
#                 ups.append(i)
#     return ups


# def recu_ret(list_, len):
#     if len(list_) == 1:
#         return list_
#     else:
#         return

# [list(int(x) for x in j if x != 'x') for j in pol]


print(get_up2(l))


# def find_sequences(lis: list, i: int):
#     if i == 1:
#         for item in lis:
#             return item
#     for item in range(len(lis)):



    # lens = len(lis)
    # sequences_lis = []
    # max_ = lis[0]
    # for item in range(1, lens * lens + 1):
    #     list_ = []
    #     for jtem in range(lens):
    #         if item == 1:
    #             list_.append(lis[jtem])
    #         else:
    #             if lis[jtem] > max_:
    #                 max_ = lis[item]
    #                 list_.append(lis[jtem])
    #         if len(list_) == item:
    #             sequences_lis.append(list_)
    #             list_ = []
    # return sequences_lis


# print(find_sequences(l))




itog = set()


def f(lst, cur=None, i=0):

    cur = [] if cur is None else cur
    if i == len(lst):
        if len(cur) > 1:
            itog.add(tuple(cur))
        return
    f(lst, cur, i + 1)
    for index in range(i, len(lst)):
        if cur and cur[-1] < lst[index]:
            f(lst, cur + [lst[index]], index + 1)
        elif not cur:
            f(lst, [lst[index]], index + 1)


f([1, 5, 2, 3, 4, 6, 1, 7])
print(len(itog))
print(max(itog, key=lambda x: len(x)))
print(*sorted(itog), sep='\n')
