# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        pointer = head
        while l1 != None or l2 != None:
            current_value = carry
            if l1 != None:
                current_value += l1.val
                l1 = l1.next
            
            if l2 != None:
                current_value += l2.val
                l2 = l2.next

            carry = (current_value // 10)
            value = current_value % 10
            pointer.next = ListNode(value)
            pointer = pointer.next
    
        if carry != 0:
            pointer.next = ListNode(carry)
            
        return head.next




