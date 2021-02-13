# two sum 
# [1, 2, 3, 5, 6] 8
# [3,5]  [6,2]

import math
from typing import List


def two_sum(arr: List[int], target_sum: int) -> List[List[int]]:
    num_set = set(arr)
    seen = set()

    ret = []
    for num in arr:
        if num in seen:
            continue

        complement = target_sum - num

        if complement in num_set:
            ret.append([num, complement])
            seen.add(num)
            seen.add(complement)

    print(ret)
    return ret

two_sum([1,2,3,5,6], 8)
