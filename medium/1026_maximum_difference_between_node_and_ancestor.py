# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ret = 0

        curr_node = root
        ancestors = []
        is_new = True

        while True:
            if is_new:
                for ancestor in ancestors:
                    ret = max(ret, abs(ancestor.val - curr_node.val))

            if curr_node.left:
                next_node = curr_node.left
                ancestors.append(curr_node)
                curr_node.left = None
                curr_node = next_node

                is_new = True
                continue

            if curr_node.right:
                next_node = curr_node.right
                ancestors.append(curr_node)
                curr_node.right = None
                curr_node = next_node

                is_new = True
                continue

            if (curr_node.left is None) and (curr_node.right is None):
                if not ancestors:
                    break
                else:
                    curr_node = ancestors.pop()
                    is_new = False

        return ret
