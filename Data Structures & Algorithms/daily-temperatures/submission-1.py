class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            
            curr = temperatures[i]
            for _ in range(len(stack)):
                last, index = stack[-1]
                if last < curr:
                    result[index] = i - index
                    stack.pop()
            stack.append((curr, i))
        
        return result

        