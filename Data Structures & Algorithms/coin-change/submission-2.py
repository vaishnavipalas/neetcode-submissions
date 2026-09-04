class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)

        if not coins:
            return 0

        dp[0] = 0

        coins.sort()


        for money in range(1, amount+1):

            fewest = float('inf')

            for coin in coins:

                if coin > money:
                    break

                remain = money - coin

                
                fewest = min(fewest, 1 + dp[remain])

            dp[money] = fewest

        ans = dp[amount]

        return ans if ans != float('inf') else -1

            




        