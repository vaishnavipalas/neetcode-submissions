class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # treat as a linked list, where val is the index, and next is the value at the index
        # use floyd's algo to detect a cycle in the list

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:

            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
                


        