class Solution:
    def findComplement(self, num: int) -> int:
        factor = 1
        ret = 0

        while num > 0:
            ret += factor * ((num + 1) % 2)
            factor *= 2
            num //= 2

        return ret
