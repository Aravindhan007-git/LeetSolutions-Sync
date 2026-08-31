# Count Complete Subarrays in an Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-count-complete-subarrays-in-an-array` |
| Topics | Array, Hash Table, Sliding Window |
| Solved | 2026-08-31 |
| Runtime | 526 ms (beats 28.394099999999995%) |
| Memory | 19.3 MB (beats 80.0705%) |

## Problem Statement

You are given an array `nums` consisting of **positive** integers.

We call a subarray of an array **complete** if the following condition is satisfied:

	- The number of **distinct** elements in the subarray is equal to the number of distinct elements in the whole array.

Return _the number of **complete** subarrays_.

A **subarray** is a contiguous non-empty part of an array.

 

**Example 1:**

**Input:** nums = [1,3,1,2,2]
**Output:** 4
**Explanation:** The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

**Example 2:**

**Input:** nums = [5,5,5,5]
**Output:** 10
**Explanation:** The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 2000`

## Solutions

```Python3
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        x=[]
        c=0
        l=0
        for r in range(len(nums)):
            x=nums[l:r+1]
            while len(list(set(x)))==len(list(set(nums))):
                c+=len(nums)-r
                l+=1
                x=nums[l:r+1]
        return c
```
