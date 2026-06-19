# String Matching in an Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-string-matching-in-an-array` |
| Topics | Array, String, String Matching |
| Solved | 2026-06-19 |
| Runtime | 3 ms (beats 63.976299999999995%) |
| Memory | 19.2 MB (beats 90.9449%) |

## Problem Statement

Given an array of string `words`, return all strings in_ _`words`_ _that are a substring of another word. You can return the answer in **any order**.

 

**Example 1:**

**Input:** words = ["mass","as","hero","superhero"]
**Output:** ["as","hero"]
**Explanation:** "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

**Example 2:**

**Input:** words = ["leetcode","et","code"]
**Output:** ["et","code"]
**Explanation:** "et", "code" are substring of "leetcode".

**Example 3:**

**Input:** words = ["blue","green","bu"]
**Output:** []
**Explanation:** No string of words is substring of another string.

 

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 30`

	- `words[i]` contains only lowercase English letters.

	- All the strings of `words` are **unique**.

## Hints

<details>
<summary>Hint 1</summary>

Bruteforce to find if one string is substring of another or use KMP algorithm.

</details>

## Solutions

```Python3
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=len(words)
        x=[]
        for i in range(l):
            for j in range(l):
                if words[i] in words[j] and i!=j and words[i] not in x:
                    x.append(words[i])
        return x
```
