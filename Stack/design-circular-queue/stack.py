class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.array = [None] * self.size
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if(not self.isFull()):
            self.array[self.rear % self.size] = value
            self.rear = (self.rear + 1) % self.size
            return True
        return False

    def deQueue(self) -> bool:
        if(not self.isEmpty()):
            self.array[self.front] = None
            self.front = (self.front + 1) % self.size
            return True
        return False

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.array[self.front % self.size]

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        if(self.rear == 0):
            return self.array[self.size - 1]
        return self.array[(self.rear - 1) % self.size]

    def isEmpty(self) -> bool:
        return ((self.front) % self.size == self.rear) & bool(self.array[self.front] == None)

    def isFull(self) -> bool:
        return ((self.rear) % self.size == self.front) & bool(self.array[self.rear] != None)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
