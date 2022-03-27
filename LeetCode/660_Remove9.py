class Solution:
    def newInteger(self, n: int) -> int:
        res = ""

        while n > 0:
            res = str(n % 9) + res
            n = n // 9

        return int(res)
