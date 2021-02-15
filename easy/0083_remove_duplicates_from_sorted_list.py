# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr_node = head

        while curr_node:
            tail = curr_node.next
            while tail and (tail.val == curr_node.val):
                tail = tail.next

            curr_node.next = tail
            curr_node = curr_node.next

        return head
