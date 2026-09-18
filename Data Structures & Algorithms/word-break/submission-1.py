class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        # search an initial section, and check for the rest in some memo graph

        memo = dict()
        wordDict = set(wordDict)


        def dfs(i):

            if i >= len(s):
                return True

            if s[i:] in wordDict:
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:

                j = len(word)

                if s[i:i+j] == word:

                    rest = memo.get(i+j, dfs(i+j))

                    if rest:
                        memo[i] = True
                        return True

            memo[i] = False
            return False


        return dfs(0)




        