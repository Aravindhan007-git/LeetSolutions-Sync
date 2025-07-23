# Remove Duplicates from Sorted List

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-remove-duplicates-from-sorted-list` |
| Topics | Linked List |
| Solved | 2025-07-23 |
| Runtime | 0 ms (beats 100%) |
| Memory | 10.9 MB (beats 100%) |

## Problem Statement

Given the `head` of a sorted linked list, _delete all duplicates such that each element appears only once_. Return _the linked list **sorted** as well_.

 

**Example 1:**

**Input:** head = [1,1,2]
**Output:** [1,2]

**Example 2:**

**Input:** head = [1,1,2,3,3]
**Output:** [1,2,3]

 

**Constraints:**

	- The number of nodes in the list is in the range `[0, 300]`.

	- `-100 <= Node.val <= 100`

	- The list is guaranteed to be **sorted** in ascending order.

## Solutions

```C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL)
        return NULL;
    struct ListNode* temp = head;
    while (temp != NULL && temp->next != NULL) {
        if (temp->val == temp->next->val) {
            temp->next = temp->next->next;
        } else {
            temp = temp->next;
        }
    }
    return head;
}
```
