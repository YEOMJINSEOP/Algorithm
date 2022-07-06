# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]):
        
        root = prev = ListNode()
        curr = head
        prev.next = curr
    
        while curr and curr.next:
            nxt = curr.next
            
            prev.next = nxt
            prev = curr
            
            curr.next = nxt.next
            curr = nxt.next
            
            nxt.next = prev
    
        return root.next
        
