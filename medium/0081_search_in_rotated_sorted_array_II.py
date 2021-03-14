class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target == nums[0]:
            return True

        # strip the right side until right side != left side
        first = nums[0]

        while len(nums) and nums[-1] == nums[0]:
            nums.pop()

        # if nums is empty now, return False
        if len(nums) == 0:
            return False

        # now we assume that nums has stuff in it
        if target < first:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                num = nums[mid]

                if num == target:
                    return True

                if num < first:
                    if target > num:
                        left = mid + 1
                    else:
                        right = mid - 1

                elif num >= first:
                    left = mid + 1

        elif target > nums[0]:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                num = nums[mid]

                if num == target:
                    return True

                if num < first:
                    right = mid - 1

                elif num >= first:
                    if target > num:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False

