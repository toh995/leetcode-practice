class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for offset in range(math.ceil(n/2)):
            min_index = offset
            max_index = n - offset - 1

            for i in range(min_index, max_index):
                j = min_index

                curr_val = matrix[i][j]
                for _ in range(4):
                    old_i = i
                    i = j
                    j = n - old_i - 1

                    next_val = matrix[i][j]
                    matrix[i][j] = curr_val
                    curr_val = next_val
