# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        odd_tail = head
        even_head = even_tail = head.next

        while odd_tail.next is not None:
            odd_tail.next = even_tail.next

            if odd_tail.next is not None:
                odd_tail = odd_tail.next
                even_tail.next = odd_tail.next

            if even_tail.next is not None:
                even_tail = even_tail.next

        odd_tail.next = even_head

        return head
