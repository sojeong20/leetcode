# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        d = []
        node = head
        
        while node:
            d.append(node.val)
            node = node.next
        
        while len(d) > 1:
            if d.pop(0) != d.pop():
                return False
        
        return True
            