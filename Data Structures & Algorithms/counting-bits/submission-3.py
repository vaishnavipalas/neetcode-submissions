class Solution:
    def countBits(self, n: int) -> List[int]:


        # iterate through each i from 0 to n
        # if i is 2 to the power of something, it will have only 1 bit
        # otherwise, find the most recent 2 to the power of something and add
        #   that plus the difference from i to that


        res = [0] * (n+1)

        powOfTwo = 1


        for i in range(1, n+1):

            if powOfTwo * 2 == i:
                powOfTwo = i

            res[i] = 1 + res[i- powOfTwo]
            



        return res






        