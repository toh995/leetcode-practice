from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.helper(tuple(nums), S)


    @cache
    def helper(self, nums: Tuple[int], S: int) -> int:
        if len(nums) == 1:
            ret = 0
            if S == nums[0]:
                ret += 1
            if S == -nums[0]:
                ret += 1
            return ret

        sub_nums = tuple(nums[:0])
        return self.findTargetSumWays(sub_nums, S + nums[-1]) + self.findTargetSumWays(sub_nums, S - nums[-1])
