# Minimum Size Subarray Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-size-subarray-sum` |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Solved | 2026-09-11 |
| Solve Time | 35m 58s |
| Runtime | 20 ms (beats 29.039200000000022%) |
| Memory | 30.5 MB (beats 79.04239999999999%) |

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return _the **minimal length** of a __subarray__ whose sum is greater than or equal to_ `target`. If there is no such subarray, return `0` instead.

 

**Example 1:**

**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

**Example 2:**

**Input:** target = 4, nums = [1,4,4]
**Output:** 1

**Example 3:**

**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0

 

**Constraints:**

	- `1 <= target <= 109`

	- `1 <= nums.length <= 105`

	- `1 <= nums[i] <= 104`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solutions

```Python3
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        size = float('inf')
        n = len(nums)
        c_s = 0
        for right in range(n):
            c_s += nums[right]
            while c_s >= target:
                size = min(size,right - left +1 )
                c_s-=nums[left]
                left+=1
        if size != float('inf'):
            return size
        else:
            return 0

```
