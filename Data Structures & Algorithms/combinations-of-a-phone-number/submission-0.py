class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        curr = []

        letters = {

            '1': [],
            '2': ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": []
        }


        def backtrack(i):

            if len(curr) == len(digits):
                if curr:
                    res.append("".join(curr))
                return

            for l in letters[digits[i]]:

                curr.append(l)

                backtrack(i + 1)

                curr.pop()

        backtrack(0)
        return res


            
        