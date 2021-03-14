class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''
        Multiple decreases:
        not touching at all => NOT POSSIBLE

        touching each other (i.e. 3+ consecutive decreases)
        [1,3,4,2,1,2]
            CASE 1: change left => then, we still have an untouched decrease - NOT POSSIBLE
            CASE 2: change right => then, the second decrease still exists - NOT POSSIBLE

        change left
            (left left) <= right
        change right
            (left) <= right right


        left edge:
        change the edge piece to match the second-to edge (i.e. change 4 to 1)
        [4,1,2]

        right edge:
        change the edge piece to match the second-to edge (i.e. change 2 to 4)
        [1,4,2]

        '''
        modified = False

        for i in range(len(nums) - 1):
            # if it's not a decrease, then just continue
            if nums[i] <= nums[i+1]:
                continue

            # here we assume we have a decrease now
            # if we've seen a decrease already, then we must return False
            elif modified:
                return False

            # if we have an edge piece, then this is a "fixable" decrease
            # continue to next iteration
            elif (i == 0) or (i+1 == len(nums)-1):
                modified = True
                continue

            # we are not on an edge piece, so check if this is fixable
            # fix by changing the left side
            elif nums[i-1] <= nums[i+1]:
                modified = True
                continue

            # fix by changing the right side
            elif nums[i] <= nums[i+2]:
                modified = True
                continue

            # if it's absolutely not fixable, then return False
            else:
                return False

        return True
