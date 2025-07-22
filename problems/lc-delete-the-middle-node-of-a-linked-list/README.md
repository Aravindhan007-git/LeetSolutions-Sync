# Delete the Middle Node of a Linked List

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-delete-the-middle-node-of-a-linked-list` |
| Topics | Linked List, Two Pointers |
| Solved | 2025-07-22 |
| Runtime | 8 ms (beats 6.875%) |
| Memory | 82.5 MB (beats 100%) |

## Problem Statement

You are given the `head` of a linked list. **Delete** the **middle node**, and return _the_ `head` _of the modified linked list_.

The **middle node** of a linked list of size `n` is the `&lfloor;n / 2&rfloor;th` node from the **start** using **0-based indexing**, where `&lfloor;x&rfloor;` denotes the largest integer less than or equal to `x`.

	- For `n` = `1`, `2`, `3`, `4`, and `5`, the middle nodes are `0`, `1`, `1`, `2`, and `2`, respectively.

 

**Example 1:**

**Input:** head = [1,3,4,7,1,2,6]
**Output:** [1,3,4,1,2,6]
**Explanation:**
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

**Example 2:**

**Input:** head = [1,2,3,4]
**Output:** [1,2,4]
**Explanation:**
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

**Example 3:**

**Input:** head = [2,1]
**Output:** [2]
**Explanation:**
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

 

**Constraints:**

	- The number of nodes in the list is in the range `[1, 105]`.

	- `1 <= Node.val <= 105`

## Hints

<details>
<summary>Hint 1</summary>

If a point with a speed s moves n units in a given time, a point with speed 2 * s will move 2 * n units at the same time. Can you use this to find the middle node of a linked list?

</details>

<details>
<summary>Hint 2</summary>

If you are given the middle node, the node before it, and the node after it, how can you modify the linked list?

</details>

## Solutions

```C
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if(head==NULL|| head->next==NULL)
        return NULL;
    struct ListNode* fast=head;
    struct ListNode* slow=head;
    struct ListNode* prev=NULL;
    while(fast!=NULL && fast->next!=NULL){
        fast=fast->next->next;
        prev=slow;
        slow=slow->next;
    }
    prev->next=slow->next;
    free(slow);
    return head;
}
```
