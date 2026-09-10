# Digit Frequency Score

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-digit-frequency-score` |
| Topics | Hash Table, Math |
| Solved | 2026-09-10 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 21.782299999999992%) |

## Problem Statement

You are given an integer `n`.

The **score** of `n` is defined as the **sum** of `d * freq(d)` over all **distinct** digits `d`, where `freq(d)` denotes the number of times the digit `d` appears in `n`.

Return an integer denoting the score of `n`.

 

**Example 1:**

**Input:** n = 122

**Output:** 5

**Explanation:**

	- The digit 1 appears 1 time, contributing `1 * 1 = 1`.

	- The digit 2 appears 2 times, contributing `2 * 2 = 4`.

	- Thus, the score of `n` is `1 + 4 = 5`.

**Example 2:**

**Input:** n = 101

**Output:** 2

**Explanation:**

	- The digit 0 appears 1 time, contributing `0 * 1 = 0`.

	- The digit 1 appears 2 times, contributing `1 * 2 = 2`.

	- Thus, the score of `n` is 2.

 

**Constraints:**

	- `1 <= n <= 109`

## Solutions

```Python3
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        n = list(str(n))
        d = {}
        for v in n:
            d[v] = d.get(v,0)+1

        l = list(d.items())
        for v in l:
            x,y = v
            score += (int(x)*y)
        return score
```
