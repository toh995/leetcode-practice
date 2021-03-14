class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        points = {(i,j) for i in range(num_rows) for j in range(num_cols)}

        while len(points):
            # get a point from the set
            i, j = next(iter(points))

            # if it's water, then move on
            if grid[i][j] == 1:
                points.remove((i, j))
                continue

            # if it's land, then explore the rest of the island
            is_closed = True
            points_to_explore = [(i,j)]

            while len(points_to_explore):
                i, j = points_to_explore.pop()

                # if point is not in points, then we've seen it before; continue
                if (i,j) not in points:
                    continue

                # remove from original points set
                points.remove((i,j))

                # if it's water, then move on
                if grid[i][j] == 1:
                    continue

                # if the current island is closed, it stays closed if
                # the current point is not on a grid edge
                if is_closed: 
                    is_closed = i != 0 \
                        and j != 0 \
                        and i != num_rows-1 \
                        and j != num_cols-1

                # now, explore the neighbors of the current point
                points_to_explore += self.get_neighbors(grid, i, j)


            count += int(is_closed)

        return count


    def get_neighbors(self, grid: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
        num_rows = len(grid)
        num_cols = len(grid[0])

        neighbors = []

        if i > 0:
            neighbors.append((i-1, j))
        if i < num_rows-1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < num_cols-1:
            neighbors.append((i, j+1))

        return neighbors
