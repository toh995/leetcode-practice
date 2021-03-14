class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r_sum = sum(nums) - nums[0]
        l_sum = 0

        for i in range(len(nums) - 1):
            if r_sum == l_sum:
                return i

            r_sum = r_sum - nums[i+1]
            l_sum = l_sum + nums[i]

        # check if the last index can be pivot
        if r_sum == l_sum:
            return len(nums) - 1

        return -1
