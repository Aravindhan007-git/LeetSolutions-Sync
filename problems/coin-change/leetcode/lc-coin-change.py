class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[amount+1]*(amount+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]

                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j],dp[i][j-coins[i-1]]+1)

        if dp[n][amount] == amount+1:
                return -1
        else:
                return dp[n][amount]