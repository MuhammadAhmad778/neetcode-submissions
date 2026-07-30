# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow=head
            if head.next:
                fast=head.next.next
            else:
                return False
        else:
            return False

        while slow!=fast and fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                return False
        if slow==fast:
            return True
        else:
            return False
        