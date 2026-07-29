# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left=list1
        
        right=list2
        
        arr=ListNode()
        temp=arr
        

        while left !=None and right!=None:
            if left.val<=right.val:
                temp.next=ListNode(left.val)
                left=left.next

            else:
                temp.next=ListNode(right.val)
                right=right.next

            temp=temp.next

        while left:
            temp.next=ListNode(left.val)
            temp=temp.next
            left=left.next
        while right:
            temp.next=ListNode(right.val)
            temp=temp.next
            right=right.next
        
        return arr.next




        