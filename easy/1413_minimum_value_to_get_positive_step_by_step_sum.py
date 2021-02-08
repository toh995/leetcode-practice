class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        less_than_one = []

        rolling_sum = 0
        for num in nums:
            rolling_sum += num

            if rolling_sum < 1:
                less_than_one.append(rolling_sum)

        if less_than_one:
            minimum = min(less_than_one)
            return 1 - minimum
        else:
            return 1
