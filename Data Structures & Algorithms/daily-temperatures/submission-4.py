class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i, curr_temp in enumerate(temperatures):
            while stack and stack[-1][1] < curr_temp:
                index, prev_temp = stack.pop()
                res[index] = i - index
            stack.append([i, curr_temp])

        return res

        