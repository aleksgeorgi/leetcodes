# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # get the middle node:
        mid = self.getMid(head)
        
        # split the list left and right and sort them 
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # merge the sorted lists 
        return self.merge(left, right)
        
    def merge(self, list1, list2):
        dummyHead = ListNode(0)
        tail = dummyHead
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next # move tail forward 
        tail.next = list1 if list1 else list2
        return dummyHead.next
        
        
    def getMid(self, head):
        # Initialize two pointers, slow and fast
        slow = fast = head
        prev = None
        
        # Move slow by one step and fast by two steps
        while fast and fast.next:
            prev = slow      
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect the left half from the right half
        if prev:
            prev.next = None
        
        return slow
        
        