# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        
        list = []
        while p:
            list.append(p.val)
            p = p.next
            
        list.sort()
        
        p = head
        for i in range(len(list)):
            p.val = list[i]
            p = p.next
            
        return head
            
        
        
        