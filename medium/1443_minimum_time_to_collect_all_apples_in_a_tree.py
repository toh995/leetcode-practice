from queue import LifoQueue

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # key is a node
        # val is a list of neighbors
        tree_map = {i: [] for i in range(n)}

        for u,v in edges:
            tree_map[u].append(v)
            tree_map[v].append(u)

        # find the set of all apple nodes
        apple_nodes = {i for i in range(n) if hasApple[i] == True}

        ret = 0
        seen = {0}
        queue = LifoQueue()
        queue.put(
            (0, None, [])
        )

        while True:
            if not len(apple_nodes):
                break
            if queue.empty():
                break

            curr_node, parent_node, path = queue.get()
            path = path + [curr_node]

            # add stuff to ret
            if curr_node in apple_nodes:
                apple_nodes.remove(curr_node)

                for i in range(len(path)-1, -1, -1):
                    node = path[i]

                    if node in seen:
                        break
                    else:
                        ret += 2
                        seen.add(node)

            # add neighbors to the queue
            neighbors = tree_map[curr_node]

            for neighbor in neighbors:
                if neighbor != parent_node:
                    queue.put(
                        (neighbor, curr_node, path)
                    )

        return ret
