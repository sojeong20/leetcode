# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = temp = ListNode(0)
        
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            now_number = temp.val + l1.val + l2.val
            print("now_number:", now_number)
            if now_number >= 10:
                temp.val = (now_number - 10)
                temp.next = ListNode(1)
                temp = temp.next
            else:
                temp.val = now_number
                if l1.next or l2.next:
                    temp.next= ListNode(0)
                    temp = temp.next
                else:
                    break
            l1 = l1.next
            l2 = l2.next
            
                    
            
        return result
            