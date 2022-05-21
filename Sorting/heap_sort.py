"""堆排序
堆的向下调整特性
"""


def sift(li, low, high):
    """ :note 辅助函数，用来构建大根堆，时间复杂度为O(logn)
    :param li: 列表
    :param low: 堆的根结点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根结点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子存在并且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下挪一层
            j = 2 * i + 1
        else:  # tmp更大
            li[i] = tmp  # 把tmp放到i的位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)
    # 第一步开始构建堆
    for i in range((n - 2) // 2, -1, -1):  # 从最后一个非叶子节点开始往前推
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)
    # 当for循环结束，堆就已经构建完成了
    for i in range(n - 1, -1, -1):  # i永远指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的边界

    return li


li = [i for i in range(10)]
import random

random.shuffle(li)

print(heap_sort(li))
