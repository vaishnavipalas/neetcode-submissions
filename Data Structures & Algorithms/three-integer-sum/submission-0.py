class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(length -2):
            j = i + 1
            k = length - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                check = nums[i] + nums[j] + nums[k]
                if check == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif check < 0:
                    j += 1
                else:
                    k -= 1
        
        return result

        