import timeit


def insert_sort_gap(li, d):
    for i in range(d, len(li)):  # 因为只需要从第二位开始进行插入对比，所以索引范围从1开始
        temp = li[i]  # temp代表当前提出来的数
        j = i - d  # j是手上当前数的索引
        while j >= 0 and li[j] > temp:  # 如果结束比较手上现有的数字，即索引j=-1，或者手上当前索引的数比摸出来的数小，立即结束循环
            li[j + d] = li[j]  # 将手上当前的数字往后挪一个位置
            j -= d  # 将索引减小一个，开始下一轮比较
        li[j + d] = temp  # 当循环结束，将提出来的数insert到当前索引后一位的位置
        # print(li)


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


def insert_sort(li):
    for i in range(1, len(li)):  # 因为只需要从第二位开始进行插入对比，所以索引范围从1开始
        temp = li[i]  # temp代表当前提出来的数
        j = i - 1  # j是手上当前数的索引
        while j >= 0 and li[j] > temp:  # 如果结束比较手上现有的数字，即索引j=-1，或者手上当前索引的数比摸出来的数小，立即结束循环
            li[j + 1] = li[j]  # 将手上当前的数字往后挪一个位置
            j -= 1  # 将索引减小一个，开始下一轮比较
        li[j + 1] = temp  # 当循环结束，将提出来的数insert到当前索引后一位的位置


li = list(range(1000))
import random, copy
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

starttime = timeit.default_timer()
shell_sort(li1)
print(li1)
print(f"time spent: {timeit.default_timer() - starttime}")

starttime = timeit.default_timer()
insert_sort(li2)
print(li2)
print(f"time spent: {timeit.default_timer() - starttime}")

lst = ['id01', 'id10', 'id02', 'id12', 'id03', 'id13']
# lst_sorted = sorted(lst, key=lambda x: int(x[2:]))
# print(lst_sorted)
# lst.sort(key=lambda x: int(x[2:]))
# print(lst)
