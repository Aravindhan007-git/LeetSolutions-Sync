# Unique Middle Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-unique-middle-element` |
| Topics | Array, Counting |
| Solved | 2026-08-31 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 56.04199999999999%) |

## Problem Statement

You are given an integer array `nums` of odd length `n`.

Return `true` if the middle element of `nums` appears **exactly** once in the array. Otherwise return `false`.

 

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** true

**Explanation:**

The middle element of `nums` is 2, which appears exactly once.

Thus, the answer is `true`.

**Example 2:**

**Input:** nums = [1,2,2]

**Output:** false

**Explanation:**

The middle element of `nums` is 2, which appears twice.

Thus, the answer is `false`.

 

**Constraints:**

	- `1 <= n == nums.length <= 100`

	- `n` is odd.

	- `1 <= nums[i] <= 100`

## Solutions

```Python3
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)//2
        if nums.count(nums[n])==1:
            return True
        else:
            return False
```
