class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        start_index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                ret = max(ret, i-start_index-1)
                start_index = i

        # consider the case where the last number is 1
        if nums[-1] == 1:
            ret = max(ret, len(nums)-start_index-1)

        return ret
