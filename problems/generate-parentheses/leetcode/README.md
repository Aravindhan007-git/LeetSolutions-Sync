# Generate Parentheses

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-generate-parentheses` |
| Topics | String, Dynamic Programming, Backtracking, Bracket Sequences |
| Solved | 2026-09-02 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 73.62280000000001%) |

## Problem Statement

Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

 

**Example 1:**

**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]
**Example 2:**

**Input:** n = 1
**Output:** ["()"]

 

**Constraints:**

	- `1 <= n <= 8`

## Solutions

```Python3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def find(s,op,cl,res):
            if len(s)==n*2:
                res.append(s)
                return
            if op<n:
                find(s+'(',op+1,cl,res)
            if cl<op:
                find(s+')',op,cl+1,res)
        find("",0,0,res)
        return res
```
