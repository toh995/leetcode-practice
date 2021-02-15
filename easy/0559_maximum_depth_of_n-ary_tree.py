"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0

        self.max_val = 0
        self.DFS(root, 0)

        return self.max_val

    def DFS(self, node: Node, path_length: int) -> None:
        # increment path length (this is our way of including our current node into the path we are traversing)
        path_length += 1

        if len(node.children) == 0:
            self.max_val = max(self.max_val, path_length)

        else:
            for child in node.children:
                if child:
                    self.DFS(child, path_length)
