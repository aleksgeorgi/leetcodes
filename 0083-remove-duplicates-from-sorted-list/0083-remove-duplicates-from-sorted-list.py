# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # check for empty list
        if head is None:
            return head

        current = head
        
        while current.next is not None:
            if current.val == current.next.val:
                # skip the next node since it's a duplicate
                current.next = current.next.next
            else:
                # move to the next node if it's not a duplicate
                current = current.next

        return head
        