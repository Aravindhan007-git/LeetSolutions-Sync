# Maximum Average Subarray I

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-maximum-average-subarray-i` |
| Topics | Array, Sliding Window |
| Solved | 2026-08-31 |
| Runtime | 60 ms (beats 57.576899999999966%) |
| Memory | 28.8 MB (beats 92.8684%) |

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return _this value_. Any answer with a calculation error less than `10-5` will be accepted.

 

**Example 1:**

**Input:** nums = [1,12,-5,-6,50,3], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

**Example 2:**

**Input:** nums = [5], k = 1
**Output:** 5.00000

 

**Constraints:**

	- `n == nums.length`

	- `1 <= k <= n <= 105`

	- `-104 <= nums[i] <= 104`

## Solutions

```Python3
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        c_s=ma=sum(nums[:k])
        
        for i in range(k,len(nums)):
            c_s+=nums[i]-nums[i-k]
            ma=max(ma,c_s)
        return ma/k
```
