class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        b = 1
        length = len(numbers)

        for a in range(length):
            b = a + 1
            while b < length:
                s = numbers[a] + numbers[b]
                if s == target:
                    return [a + 1, b + 1]
                elif s < target:
                    b += 1
                else:
                    break
        

            

        