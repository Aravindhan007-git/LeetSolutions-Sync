# To Lower Case

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-to-lower-case` |
| Topics | String |
| Solved | 2026-06-22 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.2 MB (beats 46.48689999999999%) |

## Problem Statement

Given a string `s`, return _the string after replacing every uppercase letter with the same lowercase letter_.

 

**Example 1:**

**Input:** s = "Hello"
**Output:** "hello"

**Example 2:**

**Input:** s = "here"
**Output:** "here"

**Example 3:**

**Input:** s = "LOVELY"
**Output:** "lovely"

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of printable ASCII characters.

## Hints

<details>
<summary>Hint 1</summary>

Most languages support lowercase conversion for a string data type. However, that is certainly not the purpose of the problem. Think about how the implementation of the lowercase function call can be done easily.

</details>

<details>
<summary>Hint 2</summary>

**Think ASCII!**

</details>

<details>
<summary>Hint 3</summary>

Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts. Does there seem to be any pattern there? Any mathematical relationship that we can use?

</details>

## Solutions

```Python3
class Solution:
    def toLowerCase(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if 65<=ord(s[i]) and ord(s[i])<=90:
                s[i]=chr(ord(s[i])+32)
        return "".join(s)
```
