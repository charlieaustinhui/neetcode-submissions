# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        builder=dummy

        while l1 and l2: 
            if l1.val< l2.val:
                builder.next=l1
                l1=l1.next
            else: 
                builder.next=l2
                l2=l2.next
            builder=builder.next
        if l1: 
            builder.next=l1
        if l2:
            builder.next=l2
        return dummy.next