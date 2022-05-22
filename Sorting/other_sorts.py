# 计数排序
# 限制条件：对列表进行排序，已知列表中的数的范围，必须整数
# 时间复杂度O(n)
# 空间复杂度为O(n)
def count_sort(li, max_count):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


def sys_sort(li):
    li.sort()


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建n个桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var放到几号桶里
        buckets[i].append(var)
        # 保持桶内顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    li.clear()
    for bucket in buckets:
        li.extend(bucket)


def radix_sort(li):
    max_num = max(li)  # 循环次数由最大数的位数决定
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        it += 1


import random, timeit, copy
max_count = 100
li = [random.randint(0, max_count) for _ in range(100)]
# print(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)
li4 = copy.deepcopy(li)

starttime = timeit.default_timer()
count_sort(li1, max_count)
print(f"Count sort time: {timeit.default_timer() - starttime}")

starttime = timeit.default_timer()
sys_sort(li2)
print(f"Sys sort time: {timeit.default_timer() - starttime}")


bucket_sort(li3, n=10, max_num=max_count)
print(li3)

radix_sort(li4)
print(li4)