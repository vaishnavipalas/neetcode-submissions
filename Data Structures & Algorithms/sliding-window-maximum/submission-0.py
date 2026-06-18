import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        window = []

        
        for r in range(k):
            heapq.heappush(window, -nums[r])

        result.append(-window[0])

        left = 0
        
        for right in range(k, len(nums)):
            window.remove(-nums[left])
            heapq.heapify(window)
            heapq.heappush(window, -nums[right])
            result.append(-window[0])
            left += 1

        return result





        