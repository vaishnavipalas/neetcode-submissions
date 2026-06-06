class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0
        total = 0

        l = 0
        r = len(height) -1
        maxLeft = height[l]
        maxRight = height[r]


        while l < r:

            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
        
        return total
        