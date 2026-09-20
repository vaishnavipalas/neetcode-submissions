class Solution:
    def trap(self, height: List[int]) -> int:


        max_left = 0
        max_right = 0

        l= 0
        r = len(height) - 1

        water = 0

        leftMax= [0]*len(height)
        leftMax[0] = height[0]

        for i in range(1, len(height)):

            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * len(height)
        rightMax[len(height)-1] = height[len(height) - 1]

        for j in range(len(height)- 2, -1, -1):
            rightMax[j] = max(rightMax[j+1], height[j])


        ans = 0

        for bar in range(len(height)):

            ans += min(leftMax[bar], rightMax[bar]) - height[bar]

        return ans



        