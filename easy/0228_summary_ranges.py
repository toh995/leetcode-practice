class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ret = []

        left = right = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num == (right+1):
                right = num

            else:
                to_append = str(right) if (left == right) else f"{left}->{right}"
                ret.append(to_append)

                left = right = num

        # do one more append at the end
        to_append = str(right) if (left == right) else f"{left}->{right}"
        ret.append(to_append)

        return ret
