# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None # keep track of prev node for reversing the list 
        curr = head 

        while curr:
            next_temp = curr.next
            curr.next = prev # reverse the pointer
            prev = curr # update the new previous node 
            curr = next_temp # terminates when null

        return prev

        