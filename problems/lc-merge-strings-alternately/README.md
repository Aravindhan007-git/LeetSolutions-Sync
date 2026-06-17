# Merge Strings Alternately

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-merge-strings-alternately` |
| Topics | Two Pointers, String |
| Solved | 2026-06-17 |
| Runtime | 47 ms (beats 45.38040000000001%) |
| Memory | 19.1 MB (beats 88.9231%) |

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.



Return _the merged string._



 


**Example 1:**




**Input:** word1 = "abc", word2 = "pqr"
**Output:** "apbqcr"
**Explanation:** The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


**Example 2:**




**Input:** word1 = "ab", word2 = "pqrs"
**Output:** "apbqrs"
**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


**Example 3:**




**Input:** word1 = "abcd", word2 = "pq"
**Output:** "apbqcd"
**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


 


**Constraints:**




	- `1 <= word1.length, word2.length <= 100`

	- `word1` and `word2` consist of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.

</details>

## Solutions

```Python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        i=j=0
        s=''
        while i<len(word1) and j<len(word2):
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        if j==len(word2):
            while i<len(word1):
                s+=word1[i]
                i+=1
        else:
            while j<len(word2):
                s+=word2[j]
                j+=1
        return s
```
