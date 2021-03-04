class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_point = (0,0)
        seen = set({curr_point})

        for char in path:
            # move the curr_point
            x,y = curr_point

            if char == "N":
                curr_point = (x, y+1)
            elif char == "S":
                curr_point = (x, y-1)
            elif char == "E":
                curr_point = (x+1, y)
            elif char == "W":
                curr_point = (x-1, y)

            # check the current point
            if curr_point in seen:
                return True
            else:
                seen.add(curr_point)

        return False
