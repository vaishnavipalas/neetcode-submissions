# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half

        curr= slow.next
        slow.next = None

        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev

        while second:
            temp1 = first.next
            first.next = second
            first = temp1
            temp2 = second.next
            second.next = first
            second = temp2
        


             