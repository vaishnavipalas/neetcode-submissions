class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0


        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break


        dup = 0


        while True:

            slow = nums[slow]
            dup = nums[dup]

            if dup == slow:
                return dup

        