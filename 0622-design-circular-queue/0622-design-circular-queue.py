class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.size = k
        for i in range(self.size):
            self.q.append(None)
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
        return False

    def deQueue(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.size
            return True
        return False

    def Front(self) -> int:
        if self.q[self.front] is not None:
            return self.q[self.front]
        return -1

    def Rear(self) -> int:
        if self.q[self.rear - 1] is not None:
            return self.q[self.rear - 1]
        return -1
        

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.rear] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()