# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''           
        idea: 
        iterating forward over l1 and l2
        at each step, 
            sum = the current node of each the list + the val of the carry over 
            check if the sum > 9
                yes: update the carry over to the carry over value 
                    (ex 9+9 = 18 so  insertion value is sum%10 
                        carry over is sum/10=1, 
                    ex2; 9+8 = 17sum, 17%10 = 7, 17/10 = 1carry over )
                no: insert the value at the end of the linked list
                    and reset the carry over to 0
        after the last list element has been summed check the carry over
            if it's > 0 insert the value at the end
        return the new list 
        '''
        # initialize a current node to dummy head of the returning list 
        dummy_head = ListNode(0) # create a new node and store the value 0
        current_node = dummy_head
        carry_over = 0

        # keep looping while all conditions are true 
        # l1 and l2 are pointers to the head nodes of the linked lists 
        while (l1 != None or l2 != None or carry_over != 0):
            # check for values left
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
                
            # perform the operations
            column_sum = l1_val + l2_val + carry_over
            carry_over = column_sum//10 
            
            # create the new node
            new_node = ListNode(column_sum%10)
            current_node.next = new_node
            current_node = new_node 
            
            # move the linked list nodes forward
            # if there is no next node, set the pointer of the node = None
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            
        return dummy_head.next
            
            


            
            
            
            
            
            
            
            
            
            
            
            