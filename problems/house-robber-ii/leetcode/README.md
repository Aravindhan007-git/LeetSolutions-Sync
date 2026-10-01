# House Robber II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-house-robber-ii` |
| Topics | Dynamic Programming, Array |
| Solved | 2026-10-01 |
| Solve Time | 35m 58s |
| Runtime | 3 ms (beats 7.822399999999993%) |
| Memory | 19.4 MB (beats 32.0621%) |

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

 

**Example 1:**

**Input:** nums = [2,3,2]
**Output:** 3
**Explanation:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

**Example 2:**

**Input:** nums = [1,2,3,1]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

**Example 3:**

**Input:** nums = [1,2,3]
**Output:** 3

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 1000`

## Solutions

```Python3
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n<=2:
            return max(nums)
        dpf = [0]*n
        dpf[1] = nums[1]
        for i in range(2,n):
            dpf[i] = max(dpf[i-1],nums[i]+dpf[i-2])
        
        dpl = [0]*n
        dpl[0] = nums[0]
        dpl[1] = max(nums[0],nums[1])
        for i in range(2,n-1):
            dpl[i] = max(dpl[i-1],nums[i]+dpl[i-2])

        for v in dpl:
            dpf.append(v)

        return max(dpf)
```
