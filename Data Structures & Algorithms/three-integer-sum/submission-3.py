class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        Understand - input is a list of numbers, output should be a list of lists of three numbers
        the indices of these three numbers should be different
        all the three numbers should add up to exactly 0
        important - no duplicate triplets, the order doesn't matter

        Plan - approach with two pointer technique
        first sort the array
        have a for loop for each number, then use two pointers for the rest until you get an option that equals 0

        Implement
        '''
        
        nums.sort()

        result = []

        if nums[0] > 0:
            return []
        


        for i in range(len(nums) - 1):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) -1

            while j < k:

                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
                



