class Solution:
    def isHappy(self, n: int) -> bool:

        
        seen = set()

        def happy(n):

            if n == 1:
                return True

            if n in seen:
                return False

            seen.add(n)

            s = 0

            while n:

                s += (n % 10) ** 2
                n = n // 10

            return happy(s)

        return happy(n)


        
        