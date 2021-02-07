class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        # i_max_dict and j_max_dict are dictionaries, such that:
        # key is a row/column index
        # value is the max value
        i_max_dict = {}
        j_max_dict = {}

        # populate i_max_dict and j_max_dict
        for i in range(num_rows):
            row = grid[i]
            i_max_dict[i] = max(row)

        for j in range(num_cols):
            column = [row[j] for row in grid]
            j_max_dict[j] = max(column)

        # for each cell, the new value should be the minimum of the two max values
        ret = 0

        for i in range(num_rows):
            for j in range(num_cols):
                i_max = i_max_dict[i]
                j_max = j_max_dict[j]

                max_val = min(i_max, j_max)
                cell_val = grid[i][j]

                ret += (max_val-cell_val)

        return ret
