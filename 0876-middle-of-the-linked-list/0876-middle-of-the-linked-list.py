# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None:
            return head
        
        nodeCount = 1 
        dummyHead = head
        
        while head.next != None:
            head = head.next
            nodeCount += 1
            
        # get the middle "index"    
        nodeCount = nodeCount // 2
        
        while nodeCount > 0:
            nodeCount -= 1
            dummyHead = dummyHead.next
        
        return dummyHead
        