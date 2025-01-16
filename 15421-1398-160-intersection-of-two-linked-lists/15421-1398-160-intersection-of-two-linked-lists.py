# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_b = set()

        # add B list to hashset for easy lookup
        while headB is not None:
            nodes_in_b.add(headB)
            headB = headB.next

        # check if nodes in A are in B
        while headA is not None:
            if headA in nodes_in_b:
                return headA
            headA = headA.next

        return None

        