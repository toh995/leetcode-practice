# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]

        while len(stack):
            left, right = stack.pop()

            if (not left) or (not right):
                if left != right:
                    return False

            else:
                if left.val != right.val:
                    return False

                stack.append((left.left, right.right))
                stack.append((left.right, right.left))

        return True


    # recursive    
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(left: TreeNode, right: TreeNode) -> bool:
            if (not left) or (not right):
                return left == right

            return left.val == right.val \
                and compare(left.left, right.right) \
                and compare(left.right, right.left)

        return compare(root.left, root.right)
