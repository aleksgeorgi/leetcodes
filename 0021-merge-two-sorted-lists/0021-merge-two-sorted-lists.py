# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                
        ''' my idea:
        
        iterate through both lists simultaenously 
        if you reach the end of one list, 
            append the rest of the second list at the end
        append the smallest node to the end of the list 
        '''
        # create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy

        # iterate through both lists until one empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move the tail pointer
            tail = tail.next

        # Append the remaining nodes of list1 or list2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the head of the merged list
        return dummy.next