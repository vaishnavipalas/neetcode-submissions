class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        for j in range(length-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        print(left)
        print(right)
        result = []
        for x in range(length):
            result.append(left[x]* right[x])
        return result

        