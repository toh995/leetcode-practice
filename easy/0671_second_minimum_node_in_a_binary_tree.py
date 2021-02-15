# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        second_min = self.helper(root, root.val, float("inf"))

        if second_min == float("inf"):
            return -1
        else:
            return second_min

    def helper(self, root: TreeNode, min_val: int, second_min: int) -> int:
        if root.left is None:
            return second_min

        if (root.left.val != min_val) or (root.right.val != min_val):
            new_val = max(root.left.val, root.right.val)
            second_min = min(second_min, new_val)

        if root.left.val == min_val:
            new_val = self.helper(root.left, min_val, second_min)
            second_min = min(second_min, new_val)

        if root.right.val == min_val:
            new_val = self.helper(root.right, min_val, second_min)
            second_min = min(second_min, new_val)

        return second_min

