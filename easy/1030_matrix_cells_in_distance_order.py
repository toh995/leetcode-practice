class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [[r0, c0]]

        max_row_distance = max(r0, abs(r0 - (R - 1)))
        max_col_distance = max(c0, abs(c0 - (C - 1)))

        max_distance = max_row_distance + max_col_distance

        for distance in range(1, max_distance + 1):
            r_start = max(0, r0 - distance)
            r_end = min(R-1, r0 + distance)

            for r in range(r_start, r_end + 1):
                c_delta = distance - abs(r0 - r)

                if c_delta == 0:
                    ret.append([r, c0])
                    continue

                if 0 <= c0 + c_delta < C:
                    ret.append([r, c0 + c_delta])

                if 0 <= c0 - c_delta < C:
                    ret.append([r, c0 - c_delta])

        return ret
