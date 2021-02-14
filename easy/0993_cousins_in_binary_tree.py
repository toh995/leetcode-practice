# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if (not root) or (root.val in (x, y)):
            return False

        parents = [root]
        targets = (x, y)

        while True:
            # store the parent(s) that have a child matching x and/or y
            # if both of a parent's children correspond with x and y, then that parent will appear twice here.
            matches = []

            # store the next level's parents
            next_parents = []

            for parent in parents:
                children = [parent.left, parent.right]

                for child in children:
                    if not child:
                        continue

                    next_parents.append(child)

                    if child.val in targets:
                        matches.append(parent)

            num_matches = len(matches)

            if num_matches == 2:
                return matches[0] != matches[1]

            if num_matches == 1:
                return False

            if num_matches == 0:
                parents = next_parents
                continue

        return False
