# Sort Even and Odd Indices Independently

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-sort-even-and-odd-indices-independently` |
| Topics | Array, Sorting |
| Solved | 2026-06-25 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 25.155200000000008%) |

## Problem Statement

You are given a **0-indexed** integer array `nums`. Rearrange the values of `nums` according to the following rules:

	- Sort the values at **odd indices** of `nums` in **non-increasing** order.

	
		For example, if `nums = [4,**1**,2,**3**]` before this step, it becomes `[4,**3**,2,**1**]` after. The values at odd indices `1` and `3` are sorted in non-increasing order.

	
	
	- Sort the values at **even indices** of `nums` in **non-decreasing** order.
	
		For example, if `nums = [**4**,1,**2**,3]` before this step, it becomes `[**2**,1,**4**,3]` after. The values at even indices `0` and `2` are sorted in non-decreasing order.

	
	

Return _the array formed after rearranging the values of_ `nums`.

 

**Example 1:**

**Input:** nums = [4,1,2,3]
**Output:** [2,3,4,1]
**Explanation:** 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,**1**,2,**3**] to [4,**3**,2,**1**].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [**4**,1,**2**,3] to [**2**,3,**4**,1].
Thus, the array formed after rearranging the values is [2,3,4,1].

**Example 2:**

**Input:** nums = [2,1]
**Output:** [2,1]
**Explanation:** 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## Hints

<details>
<summary>Hint 1</summary>

Try to separate the elements at odd indices from the elements at even indices.

</details>

<details>
<summary>Hint 2</summary>

Sort the two groups of elements individually.

</details>

<details>
<summary>Hint 3</summary>

Combine them to form the resultant array.

</details>

## Solutions

```Python3
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e=sorted(e)
        o=sorted(o,reverse=True)
        y=[]
        for i in range(len(nums)//2):
            y.append(e[i])
            y.append(o[i])
        if len(nums)%2!=0:
            y.append(e[-1])
        return y
```
