# Permutation in String

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-permutation-in-string` |
| Topics | String, Hash Table, Two Pointers, Sliding Window |
| Solved | 2026-06-25 |
| Runtime | 15 ms (beats 80.73200000000001%) |
| Memory | 19.2 MB (beats 97.6776%) |

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

**Example 1:**

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

**Example 2:**

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 104`

	- `s1` and `s2` consist of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Obviously, brute force will result in TLE. Think of something else.

</details>

<details>
<summary>Hint 2</summary>

How will you check whether one string is a permutation of another string?

</details>

<details>
<summary>Hint 3</summary>

One way is to sort the string and then compare. But, Is there a better way?

</details>

<details>
<summary>Hint 4</summary>

If one string is a permutation of another string then they must have one common metric. What is that?

</details>

<details>
<summary>Hint 5</summary>

Both strings must have same character frequencies, if  one is permutation of another. Which data structure should be used to store frequencies?

</details>

<details>
<summary>Hint 6</summary>

What about hash table?  An array of size 26?

</details>

## Solutions

```Python3
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        a=[0]*26
        b=[0]*26
        w=len(s1)
        r=len(s2)
        if w>r:
            return False
        for i in s1:
            a[ord(i)-ord('a')]+=1
        for i in range(r):
            if i<w:
                b[ord(s2[i])-ord('a')]+=1
            else:
                b[ord(s2[i-w])-ord('a')]-=1
                b[ord(s2[i])-ord('a')]+=1
            if a==b:
                return True
        return False
```
