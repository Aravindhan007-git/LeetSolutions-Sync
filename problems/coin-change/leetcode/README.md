# Coin Change

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-coin-change` |
| Topics | Dynamic Programming, Array, Breadth-First Search, Knapsack Problem, Complete Knapsack |
| Solved | 2026-09-29 |
| Solve Time | 35m 58s |
| Runtime | 891 ms (beats 20.34759999999988%) |
| Memory | 21.1 MB (beats 29.114900000000006%) |

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

**Example 1:**

**Input:** coins = [1,2,5], amount = 11
**Output:** 3
**Explanation:** 11 = 5 + 5 + 1

**Example 2:**

**Input:** coins = [2], amount = 3
**Output:** -1

**Example 3:**

**Input:** coins = [1], amount = 0
**Output:** 0

 

**Constraints:**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 231 - 1`

	- `0 <= amount <= 104`

## Solutions

```Python3
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
```
