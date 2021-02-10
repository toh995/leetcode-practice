# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative solution
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []

        if root is None:
            return ret

        curr_node = root
        prev_nodes = []

        while True:
            if curr_node.left:
                next_node = curr_node.left
                curr_node.left = None
                prev_nodes.append(curr_node)
                curr_node = next_node
                continue

            ret.append(curr_node.val)

            if curr_node.right:
                curr_node = curr_node.right
                continue

            if (curr_node.left is None) and (curr_node.right is None):
                if prev_nodes:
                    curr_node = prev_nodes.pop()
                else:
                    break

        return ret


    # recursive solution
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        nums = []
        self.helper(root, nums)
        return nums


    def helper(self, root: TreeNode, nums: List[int]) -> None:
        if root is None:
            return

        if root.left:
            self.helper(root.left, nums)

        nums.append(root.val)

        if root.right:
            self.helper(root.right, nums)
