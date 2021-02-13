# two sum 
# [1, 2, 3, 5, 6] 8
# [3,5]  [6,2]

'''
duplicates
same pair, different order
'''

import math
from typing import List

def two_sum(arr: List[int], target_sum: int) -> List[List[int]]:
    if len(arr) < 2:
        return []

    # n log(n)
    arr.sort()

    ret = []

    for i in range(len(arr)):
        complement = target_sum - arr[i]

        if complement <= arr[i]:
            left = 0
            right = i-1
        else:
            left = i+1
            right = len(arr) - 1

        while left <= right:
            mid = math.floor((left+right) / 2)

            if arr[mid] == complement:
                ret.append([arr[i], complement])
                break
            elif complement < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    print(ret)
    return ret

two_sum([1,2,3,5,6], 8)
