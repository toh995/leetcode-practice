class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # k is the level that the current label sits on
        k = math.log(label, 2)
        k = math.floor(k)

        # build ret array
        ret = [None] * (k+1)
        ret[-1] = label

        for i in range(k, 0, -1):
            # reassign label to its parent
            label = (((2**(i+1) - 1) - label) // 2) + 2**(i-1)
            ret[i-1] = label

        return ret
