class Solution:
    # exclusive or
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result

    # the only single number is (2 * sum of all unique numbers - sum of all numbers)
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
