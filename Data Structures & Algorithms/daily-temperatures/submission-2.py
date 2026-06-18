class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # if not stack:
            #     stack.append((temperatures[i], i))
            #     continue
            
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                last, index = stack[-1]
                result[index] = i - index
                stack.pop()
            stack.append((curr, i))
        
        return result

        