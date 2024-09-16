# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # add all the nodes to a stack 
        stack = []
        current = head
        
        while current is not None:
            stack.append(current) # pushing a reference to the ListNode object
            current = current.next
            
        current = stack.pop() # 8 
        maximum = current.val
        result_list = ListNode(maximum) # last elem is trivially a max bc nothing to the right to disqualify it
        
        # remove nodes from the stack and add to result 
        while stack:
            current = stack.pop() # 3
            if current.val < maximum:
                continue # do nothing, allow it to pop
            # add the new node to the front of the resut 
            else:
                # create a new node to append
                new_node = ListNode(current.val) 
                # point the new node to the result list head
                new_node.next = result_list
                # set the head to the new node 
                result_list = new_node 
                # update the maximum to the current.val max 
                maximum = current.val
                
        return result_list
