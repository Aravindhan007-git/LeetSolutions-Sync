# Add Digits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-digits` |
| Topics | Math, Simulation, Number Theory |
| Solved | 2026-05-04 |
| Runtime | 1 ms (beats 22.8857%) |
| Memory | 19.1 MB (beats 97.8464%) |

## Problem Statement

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

 

**Example 1:**

**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

**Example 2:**

**Input:** num = 0
**Output:** 0

 

**Constraints:**

	- `0 <= num <= 231 - 1`

 

**Follow up:** Could you do it without any loop/recursion in `O(1)` runtime?

## Hints

<details>
<summary>Hint 1</summary>

A naive implementation of the above process is trivial. Could you come up with other methods?

</details>

<details>
<summary>Hint 2</summary>

What are all the possible results?

</details>

<details>
<summary>Hint 3</summary>

How do they occur, periodically or randomly?

</details>

<details>
<summary>Hint 4</summary>

You may find this Wikipedia article useful.

</details>

## Solutions

```Python3
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return num
        
        while num>=10:
            sum=0
            while num>0:
                sum=sum+(num%10)
                num=num//10
            num=sum
        return num
```
