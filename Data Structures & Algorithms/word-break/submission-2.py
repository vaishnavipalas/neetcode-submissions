class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        words = set(wordDict)

        dp = [False] * (len(s) + 1)

        dp[0] = True



        for curr in range(1, len(s) + 1):

            for i in range(curr):

                if dp[i] and s[i:curr] in words:

                    dp[curr] = True

        return dp[-1]