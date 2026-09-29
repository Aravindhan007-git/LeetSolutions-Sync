class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        
        dp[0] = 1

        for c in coins:
            for j in range(c,amount+1):
                dp[j]+=dp[j-c]

        return dp[amount]