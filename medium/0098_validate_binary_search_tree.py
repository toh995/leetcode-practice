# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def isValidBST1(self, root: TreeNode) -> bool:
        return self.helper(root, float("inf"), float("-inf"))

    def helper(self, pointer: TreeNode, upper_bound: int, lower_bound: int) -> bool:
        if pointer is None:
            return True

        if (not pointer.left) and (not pointer.right):
            return True

        if pointer.left:
            left_upper_bound = min(pointer.val, upper_bound)
            left_lower_bound = lower_bound

            if (pointer.left.val >= left_upper_bound) \
                or (pointer.left.val <= left_lower_bound):
                return False

        if pointer.right:
            right_upper_bound = upper_bound
            right_lower_bound = max(pointer.val, lower_bound)

            if (pointer.right.val >= right_upper_bound) \
                or (pointer.right.val <= right_lower_bound):
                return False

        return self.helper(pointer.left, min(pointer.val, upper_bound), lower_bound) \
            and self.helper(pointer.right, upper_bound, max(pointer.val, lower_bound))

    def isValidBST2(self, root: TreeNode) -> bool:
        # ancestors will be an array, where each entry is a hashmap.
        # populate ancestors with the root node.
        ancestors = []

        curr_node = {
            "pointer": root,
            "upper_bound": float("inf"),
            "lower_bound": float("-inf"),
        }

        while True:
            pointer = curr_node["pointer"]

            if pointer.left:
                # evaluate left pointer value
                upper_bound = min(pointer.val, curr_node["upper_bound"])
                lower_bound = curr_node["lower_bound"]
                if (pointer.left.val >= upper_bound) or (pointer.left.val <= lower_bound):
                    return False

                # move left
                ancestors.append(curr_node)
                next_pointer = pointer.left
                pointer.left = None
                curr_node = {
                    "pointer": next_pointer,
                    "upper_bound": upper_bound,
                    "lower_bound": lower_bound,
                }
                continue


            if pointer.right:
                # evaluate the right pointer value                
                upper_bound = curr_node["upper_bound"]
                lower_bound = max(pointer.val, curr_node["lower_bound"])
                if (pointer.right.val >= upper_bound) or (pointer.right.val <= lower_bound):
                    return False

                # move right
                ancestors.append(curr_node)
                next_pointer = pointer.right
                pointer.right = None
                curr_node = {
                    "pointer": next_pointer,
                    "upper_bound": upper_bound,
                    "lower_bound": lower_bound,
                }
                continue

            if (not pointer.left) and (not pointer.right):
                if not ancestors:
                    break
                else:
                    # move up to the parent
                    curr_node = ancestors.pop()

        return True
