# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-06-30 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.6 MB (beats 42.665100000000024%) |

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

**Example 1:**

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.00000
**Explanation:** merged array = [1,2,3] and median is 2.

**Example 2:**

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.50000
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

**Constraints:**

	- `nums1.length == m`

	- `nums2.length == n`

	- `0 <= m <= 1000`

	- `0 <= n <= 1000`

	- `1 <= m + n <= 2000`

	- `-106 <= nums1[i], nums2[i] <= 106`

## Solutions

```Python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1,nums2):
            i=j=0
            x=[]
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    x.append(nums1[i])
                    i+=1
                else:
                    x.append(nums2[j])
                    j+=1
            while i<len(nums1):
                x.append(nums1[i])
                i+=1
            while j<len(nums2):
                x.append(nums2[j])
                j+=1
            return x
        mer=merge(nums1,nums2)
        i,j=0,len(mer)-1
        while i<j:
            i+=1
            j-=1
        return (mer[i]+mer[j])/2
```
