class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # check the case where it's a vertical line
        if (x2 - x1) == 0:
            return all(x == x1 for x,y in coordinates)

        # otherwise, check non-vertical lines
        else:
            m = (y2-y1) / (x2-x1)
            b = y1 - m*x1

            return all(y == m*x + b for x,y in coordinates)
