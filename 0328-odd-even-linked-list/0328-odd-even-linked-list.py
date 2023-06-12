# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        result = head
        temp1 = temp2 = ListNode()
        
        while head.next and head.next.next:
            head.next, temp1.val = head.next.next, head.next.val
            temp1.next = head.next.next
            head = head.next
            temp1 = temp1.next
        
        head.next = temp2
        
        return result
            
            
        