class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.right, self.tail.left = self.tail, self.head
        self.k, self.len = k, 0

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        
        new = ListNode(value)
        right = self.head.right
        self.head.right = new
        new.left, new.right = self.head, right
        right.left = new
        
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        
        new = ListNode(value)
        left = self.tail.left
        left.right = new
        new.left, new.right = left, self.tail
        self.tail.left = new
        
        self.len += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        
        right = self.head.right.right
        self.head.right, right.left = right, self.head
        
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        
        left = self.tail.left.left
        self.tail.left, left.right = left, self.tail
        
        self.len -= 1
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
        
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


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