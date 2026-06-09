# Valid Palindrome

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-valid-palindrome` |
| Topics | String, Two Pointers |
| Solved | 2026-06-09 |
| Runtime | 7 ms (beats 81.1182%) |
| Memory | 23.4 MB (beats 12.042499999999988%) |

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`_ if it is a **palindrome**, or _`false`_ otherwise_.

 

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

**Example 3:**

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

**Constraints:**

	- `1 <= s.length <= 2 * 105`

	- `s` consists only of printable ASCII characters.

## Solutions

```Python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x="".join(ch.lower() for ch in s if ch.isalnum())
        if x==x[::-1]:
            return True
        else:
            return False

```
