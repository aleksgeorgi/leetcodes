/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        //if no elements, cannot be a cycle
        if (head==null){
            return false;
        }
        
        Set<ListNode> set = new HashSet<ListNode>();
        
        while (head != null){
            if (set.contains(head)){
                return true;
            }
            set.add(head);
            head=head.next;
        }
        return false;
    }
} 
// this gives O(n) time because we iterate through the whole list of size n and O(n) space because we're storing the whole list
