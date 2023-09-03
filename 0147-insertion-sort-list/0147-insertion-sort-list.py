# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode()
        
        while head:
            while cur.next and cur.next.val <= head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            cur = parent
            
         
        return parent.next
        
        
        