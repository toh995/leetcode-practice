class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = 0
        odds = 0

        for chip in position:
            if chip % 2 == 0:
                evens += 1
            else:
                odds += 1

        return min(evens, odds)
