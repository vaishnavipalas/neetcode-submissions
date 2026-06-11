class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr = temperatures[i]

            while stack and curr > stack[-1][1]:
                stackI, stackT = stack.pop()
                result[stackI] = i - stackI
            stack.append([i, curr])
        
        return result
        