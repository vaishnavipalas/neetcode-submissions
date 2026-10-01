# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = ListNode(0)
        curr = res

        heads = []
        heapq.heapify(heads)

        for i in range(len(lists)):

            if not lists[i]:
                continue

            heapq.heappush(heads, (lists[i].val, i))

        while heads:

            _, idx = heapq.heappop(heads)

            curr.next = lists[idx]
            lists[idx] = lists[idx].next

            if lists[idx]:
                heapq.heappush(heads, (lists[idx].val, idx))
            
            curr = curr.next

        return res.next
                    
        