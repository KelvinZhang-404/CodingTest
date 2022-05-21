"""堆排序
堆的向下调整特性
"""


def sift(li, low, high):
    """
    :note 辅助函数，用来构建小根堆，时间复杂度为O(logn)
    :param li: 列表
    :param low: 堆的根结点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根结点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子存在并且比较小
            j = j + 1  # j指向右孩子
        if li[j] < tmp:  # 如果最小的孩子比堆顶小
            li[i] = li[j]  # 将父亲和孩子对调
            i = j  # 往下挪一层
            j = 2 * i + 1  # j现在是新的左孩子，回到循环开始
        else:  # tmp更大
            li[i] = tmp  # 把tmp放到i的位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def topk(li, k):
    heap = li[0:k]  # 取列表前K个数
    # 1 建立小根堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)  # sift函数用来建立小根堆，所以此时堆顶必定是前k个数里第k大的数
    # 2 循环比较剩下的数与堆顶数字
    for i in range(k, len(li)):
        if li[i] > heap[0]:  # 如果当前数比堆顶数大，证明堆顶肯定不是第K大的数
            heap[0] = li[i]  # 将堆顶数字设成当前数字
            sift(heap, 0, k - 1)  # 重建小根堆
    # 3 此时堆里的数已经是前K大的数字，再进行一次堆排序即可
    for i in range(k - 1, -1, -1):  # i永远指向当前堆的最后一个元素
        heap[0], heap[i] = heap[i], heap[0]  # 将堆顶放到最后
        sift(heap, 0, i - 1)  # i-1是新的边界
    return heap


li = [i for i in range(15)]
import random

random.shuffle(li)

print(topk(li, 15))

