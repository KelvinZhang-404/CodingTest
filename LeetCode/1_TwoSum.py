class Solution:
    def binary_search(self, li, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if li[mid][0] == target:
                return mid
            elif li[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])

        n = len(new_nums)
        for i in range(n):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, n - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                return [new_nums[i][1], new_nums[j][1]]
