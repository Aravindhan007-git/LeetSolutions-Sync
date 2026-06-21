# Majority Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-majority-element` |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–moore Majority Vote Algorithm |
| Solved | 2026-06-21 |
| Runtime | 4 ms (beats 71.355%) |
| Memory | 21.1 MB (beats 83.98619999999998%) |

## Problem Statement

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `&lfloor;n / 2&rfloor;` times. You may assume that the majority element always exists in the array.

 

**Example 1:**

**Input:** nums = [3,2,3]
**Output:** 3
**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 104`

	- `-109 <= nums[i] <= 109`

	- The input is generated such that a majority element will exist in the array.

 

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Solutions

```Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x={}
        new=list(set(nums))
        for i in range(len(new)):
            a=nums.count(new[i])
            x[new[i]]=a
        return max(x,key=x.get)
```
