class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)

        if not coins:
            return 0

        dp[0] = 0

        coins.sort()

        for money in range(1, amount+1):
            for coin in coins:
                remain = money - coin
                if remain >= 0:
                    dp[money] = min(dp[money], 1 + dp[remain])
        return dp[amount] if dp[amount] != float('inf') else -1

            




        