# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        import collections
        
        node = head
        d = collections.deque()
        
        while node:
            d.append(node.val)
            node = node.next
        
        while len(d) > 1:
            if d.popleft() != d.pop():
                print(d)
                return False
        
        return True
            