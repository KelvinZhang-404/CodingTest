'''
辅助函数partition用来返回分界值的索引
'''
def partition(lst, left, right):
    tmp = lst[left]  # 以最左边的数作为分界值，这个位置之后将会被替代
    while left < right:  # 当左右索引相同的时候，循环结束，所有比tmp小的都会放到左边，比tmp大的都会被放到右边
        while left < right and lst[right] >= tmp:  # 注意边界问题，每次循环都需要比较左右索引，确保指针位置正确
            right -= 1
        lst[left] = lst[right]  # 当发现右边的值比tmp小，将其替换左索引所在数字，此时右索引位置等待被替代
        while left < right and lst[left] <= tmp:
            left += 1
        lst[right] = lst[left]  # 当发现左边的值比tmp大，将其替换右索引所在数字，此时左索引位置等待被替代
    lst[left] = tmp  # 别忘了将分界索引的值替换掉
    # print(lst)
    return left  # 返回分界索引


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)  # 找到分界值所在的索引位置
        quick_sort(li, left, mid - 1)  # 递归索引左边
        quick_sort(li, mid + 1, right)  # 递归索引右边
    return li


if __name__ == '__main__':
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    quick_sort(li, 0, len(li) - 1)
    print(li)
