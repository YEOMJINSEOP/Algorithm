class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        
        self.k = k
        self.len = 0
        
        self.head.right = self.tail
        self.tail.left = self.head
    
    def isEmpty(self) -> bool:
        return self.len == 0
        
    def isFull(self) -> bool:
        return self.len == self.k
    
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        new.right = n
        n.left = new
        node.right = new
        new.left = node
    
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
    
    
    def insertFront(self, value: int) -> bool:
        if (self.isFull()):
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
            
    def insertLast(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
            
    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        self.len -= 1
        self._del(self.head)
        return True
    
    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    
    def getFront(self) -> int:
        if self.len > 0:
            return self.head.right.val
        else:
            return -1
    def getRear(self) -> int:
        if self.len > 0:
            return self.tail.left.val
        else:
            return -1
        



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
