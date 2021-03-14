class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0]
        index = 0
        reset_index = 1

        for _ in range(num):
            # check if we should reset
            if index == reset_index:
                ret.append(1)
                reset_index = reset_index * 2
                index = 1

            else:
                next_val = ret[index] + 1
                ret.append(next_val)
                index += 1

        return ret
