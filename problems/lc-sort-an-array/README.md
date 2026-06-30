# Sort an Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-sort-an-array` |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort |
| Solved | 2026-06-30 |
| Runtime | 773 ms (beats 23.0855000000007%) |
| Memory | 26.6 MB (beats 77.84250000000002%) |

## Problem Statement

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

 

**Example 1:**

**Input:** nums = [5,2,3,1]
**Output:** [1,2,3,5]
**Explanation:** After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

**Example 2:**

**Input:** nums = [5,1,1,2,0,0]
**Output:** [0,0,1,1,2,5]
**Explanation:** Note that the values of nums are not necessarily unique.

 

**Constraints:**

	- `1 <= nums.length <= 5 * 104`

	- `-5 * 104 <= nums[i] <= 5 * 104`

## Solutions

```Python3
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums,low,high):
            if low<high:
                mid=(low+high)//2
                mergesort(nums,low,mid)
                mergesort(nums,mid+1,high)
                merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            left=nums[low:mid+1]
            right=nums[mid+1:high+1]
            i=j=0
            k=low
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            return nums
        mergesort(nums,0,len(nums)-1)
        return nums
```
