from functools import cache
from math import factorial

class Solution:
    # combinatorial solution
    def uniquePaths(self, m: int, n: int) -> int:
        return int(
            factorial((m-1) + (n-1)) / (factorial(m-1) * factorial(n-1))
        )

    # recursive solution
    @cache
    def uniquePathsRecursive(self, m: int, n: int) -> int:
        if m > n:
            return self.uniquePaths(n, m)

        if 1 in (m, n):
            return 1

        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
