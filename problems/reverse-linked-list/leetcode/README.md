# Reverse Linked List

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-linked-list` |
| Topics | Linked List, Recursion |
| Solved | 2025-07-22 |
| Runtime | 0 ms (beats 100%) |
| Memory | 10.6 MB (beats 100%) |

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

 

**Example 1:**

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

**Example 2:**

**Input:** head = [1,2]
**Output:** [2,1]

**Example 3:**

**Input:** head = []
**Output:** []

 

**Constraints:**

	- The number of nodes in the list is the range `[0, 5000]`.

	- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solutions

```C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current=head;
    struct ListNode* next=NULL;
    struct ListNode* prev=NULL;
    while(current!=NULL){
        next=current ->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    return prev;
}
```
