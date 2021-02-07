from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # create a mapping where each key/value pair represents a diagonal.
        # key is the sum of the row and column indexes on the diagonal
        # value is a list of values on the diagonal (ordered appropriately)
        mapping = defaultdict(list)

        # iterate through the rows in descending order
        num_rows = len(nums)
        for i in range(num_rows-1, -1, -1):
            row = nums[i]
            num_cols = len(row)

            for j in range(num_cols):
                cell_val = nums[i][j]

                index_sum = i + j
                diagonal_list = mapping[index_sum]

                diagonal_list.append(cell_val)

        sorted_keys = sorted(mapping.keys())
        ret = []

        for key in sorted_keys:
            diagonal_list = mapping[key]
            ret += diagonal_list

        return ret
