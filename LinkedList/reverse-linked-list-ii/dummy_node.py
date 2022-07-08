# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        root = ListNode(0, head)
        
        curr = root
        for i in range(left):
            curr = curr.next
        
        leftTmp = root
        for i in range(left - 1):
            leftTmp = leftTmp.next
            
        prev = ListNode(None)
        prev.next = curr
        
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        leftTmp.next.next = curr
        leftTmp.next = prev
        
        return root.next
