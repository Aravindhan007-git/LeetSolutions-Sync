# Insert Interval

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-insert-interval` |
| Topics | Array |
| Solved | 2026-08-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 21.4 MB (beats 57.14650000000002%) |

## Problem Statement

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Two intervals are considered overlapping if they share **at least** one point.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals`_ after the insertion_.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

 

**Example 1:**

**Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Output:** [[1,5],[6,9]]

**Example 2:**

**Input:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Output:** [[1,2],[3,10],[12,16]]
**Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 

**Constraints:**

	- `0 <= intervals.length <= 104`

	- `intervals[i].length == 2`

	- `0 <= starti <= endi <= 105`

	- `intervals` is sorted by `starti` in **ascending** order.

	- `newInterval.length == 2`

	- `0 <= start <= end <= 105`

## Hints

<details>
<summary>Hint 1</summary>

Intervals Array is sorted. Can you use Binary Search to find the correct position to insert the new Interval.?

</details>

<details>
<summary>Hint 2</summary>

Can you try merging the overlapping intervals while inserting the new interval?

</details>

<details>
<summary>Hint 3</summary>

This can be done by comparing the end of the last interval with the start of the new interval and vice versa.

</details>

## Solutions

```Python3
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mer=[]
        for inter in intervals:
            s2,e2=inter
            if len(mer)==0:
                mer.append(inter)
            else:
                s1,e1=mer[-1]
                if e1>=s2:
                    mer[-1][1]=max(e1,e2)
                else:
                    mer.append(inter)
        return mer
```
