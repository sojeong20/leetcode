# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        print(left, right)
        my_list = []
        result = temp = ListNode()
        
        while head:
            my_list.append(head.val)
            head = head.next
        
        my_list[left-1: right] = reversed(my_list[left - 1: right])
        
        for i in range(len(my_list) - 1):
            temp.val = my_list[i]
            temp.next = ListNode()
            temp = temp.next
        temp.val = my_list[-1]
            
        return result