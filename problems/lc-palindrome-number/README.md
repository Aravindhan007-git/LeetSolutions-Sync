# Palindrome Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-palindrome-number` |
| Topics | Math |
| Solved | 2026-08-14 |
| Runtime | 1 ms (beats 93.3008%) |
| Memory | 19.2 MB (beats 87.22680000000001%) |

## Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

 

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

 

**Constraints:**

	- `-231 <= x <= 231 - 1`

 

**Follow up:** Could you solve it without converting the integer to a string?

## Hints

<details>
<summary>Hint 1</summary>

Beware of overflow when you reverse the integer.

</details>

## Solutions

```Python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False
```
