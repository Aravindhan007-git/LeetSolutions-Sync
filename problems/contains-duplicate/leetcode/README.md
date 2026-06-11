# Contains Duplicate

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-contains-duplicate` |
| Topics | Array, Hash Table, Sorting |
| Solved | 2026-06-11 |
| Runtime | 0 ms (beats 100%) |
| Memory | 31.3 MB (beats 93.00950000000003%) |

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-109 <= nums[i] <= 109`

## Solutions

```Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            return True
```
