# 介绍三种常见排序的方法实现
class SlowSorting:
    def __init__(self, li):
        self.li = li
        print(f"Original list: {self.li}")

    ''' 冒泡排序
    存在无序区和有序区两个区间
    每冒泡一次，无序区减少一个数字，有序区增加一个数字
    时间：O(n^2)
    '''
    def bubble_sort(self):
        li = self.li
        for i in range(len(li) - 1):  # 整个排序只需要进行n-1趟循环，i代表当前第几趟循环，从0开始
            exchange = False  # 设置一个变量来跟踪在当前冒泡过程中是否有进行过交换，初始为False
            for j in range(len(li) - i - 1):  # 代表无序区循环次数，每过一趟循环次数减1
                if li[j] > li[j + 1]:  # 如果当前索引数字比下一位数字大，则进行交换
                    li[j], li[j + 1] = li[j + 1], li[j]
                    exchange = True  # 当进行过冒泡，将exchange变为真
            print(li)
            if not exchange:  # 在每次冒泡结束的时候检查exchange，如果没有进行过交换，则代表当前无序区已经是排序数据，直接返回
                return li
        return li

    '''选择排序
    存在已排序区和未排序区
    每次循环都将找到一个未排序区最小数字，并且移动到首位
    每次循环过后未排序区少一个数，已排序区增加一个数
    时间：O(n^2)
    '''
    def select_sort(self):
        li = self.li
        for i in range(len(li) - 1):  # 整个排序只需要进行n-1次，因为最后一次可以被忽略
            min_idx = i  # 初始未排序区第一个位置为最小数索引
            for j in range(i + 1, len(li)):  # 从第二个数字开始一一与最小索引位置的数字对比
                if li[j] < li[min_idx]:  # 如果当前索引数字比最小索引数字大，则将当前索引赋值给最小索引
                    min_idx = j  # 循环一遍下来，未排序区就能找到最小数字的索引位置
            li[i], li[min_idx] = li[min_idx], li[i]  # 将未排序区第一位数字与最小数字对调
            print(li)
        return li

    '''插入排序
    存在已排序手牌和未排序手牌两个区间
    每次比较未排序手牌首位数字和已排序手牌所有数字
    时间：O(n^2)
    '''
    def insert_sort(self):
        li = self.li
        for i in range(1, len(li)):  # 因为只需要从第二位开始进行插入对比，所以索引范围从1开始
            temp = li[i]  # temp代表当前提出来的数
            j = i - 1  # j是手上当前数的索引
            while j >= 0 and li[j] > temp:  # 如果结束比较手上现有的数字，即索引j=-1，或者手上当前索引的数比摸出来的数小，立即结束循环
                li[j + 1] = li[j]  # 将手上当前的数字往后挪一个位置
                j -= 1  # 将索引减小一个，开始下一轮比较
            li[j + 1] = temp  # 当循环结束，将提出来的数insert到当前索引后一位的位置
            print(li)
        return li


if __name__ == '__main__':
    li = [1, 2, 3, 7, 5, 8, 9, 4, 6]
    slowSorting = SlowSorting(li)
    slowSorting.insert_sort()
    # slowSorting.bubble_sort()
    # slowSorting.select_sort()