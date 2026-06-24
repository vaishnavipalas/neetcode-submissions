# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        temp = head

        while temp:
            length += 1
            temp = temp.next
            

        nth = length - n

        if nth == 0:
            return head.next
        
        counter = 0
        curr = head

        while counter < nth - 1:
            curr = curr.next
            counter += 1

        curr.next = curr.next.next

        return head


        