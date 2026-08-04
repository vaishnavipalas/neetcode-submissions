class Solution:
    def partition(self, s: str) -> List[List[str]]:


        res = []
        curr = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start_idx):

            if start_idx == len(s):
                res.append(curr.copy())
                return


            for j in range(start_idx, len(s)):

                if isPalindrome(s[start_idx:j + 1]):
                    curr.append(s[start_idx:j + 1])

                    backtrack(j+1)

                    curr.pop()

        backtrack(0)

        return res

        