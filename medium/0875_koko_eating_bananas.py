class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # binary search
        left = 1
        right = ret = max(piles)

        while left <= right:
            mid = (left + right) // 2
            hours = sum(
                ceil(pile/mid) for pile in piles
            )

            if hours <= H:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1

        return ret
