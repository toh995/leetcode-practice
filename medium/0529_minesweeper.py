class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click

        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        else:
            # find number of adjacent mines
            deltas = itertools.product({-1,0,1}, {-1,0,1})

            # filter through the valid deltas we want to test for
            def is_valid_delta(delta: Tuple[int]) -> bool:
                if delta == (0, 0):
                    return False

                new_i = i + delta[0]
                new_j = j + delta[1]

                return (0 <= new_i) and (new_i < len(board)) \
                    and (0 <= new_j) and (new_j < len(board[0]))

            deltas = filter(is_valid_delta, deltas)
            deltas = list(deltas)

            num_adj_mines = sum(
                int(board[i+i_delta][j+j_delta] == "M") for i_delta,j_delta in deltas
            )

            # decide on a course of action, depending on how many adjacent mines there are
            if num_adj_mines > 0:
                board[i][j] = str(num_adj_mines)

            else:
                board[i][j] = "B"

                for i_delta, j_delta in deltas:
                    new_i = i + i_delta
                    new_j = j + j_delta

                    if board[new_i][new_j] != "B":
                        self.updateBoard(board, [new_i, new_j])

            return board
