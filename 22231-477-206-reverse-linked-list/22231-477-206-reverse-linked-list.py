# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        revList = [head.val]
        currNode = head

        while currNode.next:
            currNode = currNode.next
            revList.insert(0, currNode.val)

        currNode = head
        for i in range(len(revList)):
            currNode.val = revList[i]
            currNode = currNode.next
        return head
        