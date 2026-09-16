class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry1 = True


        for i in range(len(digits) - 1, -1, -1):

            if carry1:
                digits[i] += 1

            if digits[i] < 10:
                return digits
            else:
                print('reached')
                digits[i] =0
                carry1 = True


        if digits[0] == 0 and carry1:
            return [1] + digits
        