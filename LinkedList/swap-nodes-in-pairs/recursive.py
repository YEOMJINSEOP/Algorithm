# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]):
        
        if (head is None or head.next is None):
            return head

        
        nxt = head.next
        head.next = self.swapPairs(head.next.next)
        nxt.next = head
        
        return nxt
    

            
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        reversed_l1 = self.reverseList(l1)
        list_reversed_l1 = self.linkedListToList(reversed_l1)
        
        reversed_l1 = self.reverseList(l2)
        list_reversed_l2 = self.linkedListToList(reversed_l1)
        
        int_l1 = int(''.join(map(str,list_reversed_l1)))
        int_l2 = int(''.join(map(str,list_reversed_l2)))
        
        result = str(int_l1 + int_l2)
        return self.toReversedLinkedList(result)

        
