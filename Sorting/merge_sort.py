def merge(li, low, mid, high):
    left = low
    right = mid + 1
    ltmp = []
    while left <= mid and right <= high:  # 只要左右两边都有数
        if li[left] < li[right]:
            ltmp.append(li[left])
            left += 1
        else:
            ltmp.append(li[right])
            right += 1
    while left <= mid:
        ltmp.append(li[left])
        left += 1
    while right <= high:
        ltmp.append(li[right])
        right += 1
    li[low:high+1] = ltmp


def merge_sort(li, low, high):
    if low < high:  # 至少有两个元素
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)
        print(li[low:high+1])


def merge_sort_test(li, low, high):
    if low < high:  # 至少有两个元素
        mid = (low + high) // 2
        merge_sort_test(li, low, mid)
        merge_sort_test(li, mid + 1, high)
        print(li[low:high+1])


li = list(range(15))
import random
random.shuffle(li)

print(li)
merge_sort(li, 0, len(li)-1)
print(li)