# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = ListNode()
        while head != None and head.next != None:
            if head.next != None:
                even_head.next = head.next
            if head.next.next != None:
                head.next = head.next.next

        head.next = even_head.next
        return head