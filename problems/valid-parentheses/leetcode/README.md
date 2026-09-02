# Valid Parentheses

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-valid-parentheses` |
| Topics | String, Stack, Bracket Sequences |
| Solved | 2026-09-02 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 23.632700000000014%) |

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

 

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	- `1 <= s.length <= 104`

	- `s` consists of parentheses only `'()[]{}'`.

## Solutions

```Python3
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for v in s:
            if v=='(' or v=='{' or v=='[':
                st.append(v)
            else:
                if not st:
                    return False
                top=st.pop()
                if v==')' and top!='(':
                    return False
                elif v=='}' and top!='{':
                    return False
                elif v==']' and top!='[':
                    return False
        return len(st)==0
```
