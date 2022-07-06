# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: ListNode):
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    
    def linkedListToList(self, head: ListNode):
        
        list: List = []
        
        while head:
            list.append(head.val)
            head = head.next
        
        return list
    
    def toReversedLinkedList(self, result: str ):
        prev: ListNode = None
        for num in result:
            node = ListNode(num)
            node.next = prev
            prev = node
        
        return prev
            
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        reversed_l1 = self.reverseList(l1)
        list_reversed_l1 = self.linkedListToList(reversed_l1)
        
        reversed_l1 = self.reverseList(l2)
        list_reversed_l2 = self.linkedListToList(reversed_l1)
        
        int_l1 = int(''.join(map(str,list_reversed_l1)))
        int_l2 = int(''.join(map(str,list_reversed_l2)))
        
        result = str(int_l1 + int_l2)
        return self.toReversedLinkedList(result)

        
