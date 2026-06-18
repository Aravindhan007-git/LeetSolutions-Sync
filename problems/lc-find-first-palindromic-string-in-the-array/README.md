# Find First Palindromic String in the Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-first-palindromic-string-in-the-array` |
| Topics | Array, Two Pointers, String |
| Solved | 2026-06-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.5 MB (beats 31.570400000000006%) |

## Problem Statement

Given an array of strings `words`, return _the first **palindromic** string in the array_. If there is no such string, return _an **empty string** _`""`.

A string is **palindromic** if it reads the same forward and backward.

 

**Example 1:**

**Input:** words = ["abc","car","ada","racecar","cool"]
**Output:** "ada"
**Explanation:** The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

**Example 2:**

**Input:** words = ["notapalindrome","racecar"]
**Output:** "racecar"
**Explanation:** The first and only string that is palindromic is "racecar".

**Example 3:**

**Input:** words = ["def","ghi"]
**Output:** ""
**Explanation:** There are no palindromic strings, so the empty string is returned.

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 100`

	- `words[i]` consists only of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Iterate through the elements in order. As soon as the current element is a palindrome, return it.

</details>

<details>
<summary>Hint 2</summary>

To check if an element is a palindrome, can you reverse the string?

</details>

## Solutions

```Python3
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=0
        for i in words:
            if i==i[::-1]:
                f=1
                return i
        if not f:
            return ""

```
