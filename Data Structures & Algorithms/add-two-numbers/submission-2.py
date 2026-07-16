# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy

        carry = False
        while l1 or l2:

            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            new_val = first + second + (1 if carry else 0)

            if new_val > 9:
                carry = True
            else:
                carry = False

            new_node = ListNode(new_val % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            prev.next = new_node
            prev = prev.next

        rest = l1 if l1 else l2

        if carry:
            prev.next = ListNode(1)

        return dummy.next

            

            
        
        
            

        