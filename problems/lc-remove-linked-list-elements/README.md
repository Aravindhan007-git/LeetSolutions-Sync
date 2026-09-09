# Remove Linked List Elements

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-remove-linked-list-elements` |
| Topics | Linked List, Recursion |
| Solved | 2026-09-09 |
| Runtime | 4 ms (beats 22.3731%) |
| Memory | 22.4 MB (beats 41.98450000000001%) |

## Problem Statement

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return _the new head_.

 

**Example 1:**

**Input:** head = [1,2,6,3,4,5,6], val = 6
**Output:** [1,2,3,4,5]

**Example 2:**

**Input:** head = [], val = 1
**Output:** []

**Example 3:**

**Input:** head = [7,7,7,7], val = 7
**Output:** []

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 104]`.

	- `1 <= Node.val <= 50`

	- `0 <= val <= 50`

## Solutions

```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,next = head)
        temp = dummy
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next
```
