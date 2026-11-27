# Binary Tree Postorder Traversal

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-tree-postorder-traversal` |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Solved | 2026-11-27 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 14.787300000000009%) |

## Problem Statement

Given the `root` of a binary tree, return _the postorder traversal of its nodes' values_.

 

**Example 1:**

**Input:** root = [1,null,2,3]

**Output:** [3,2,1]

**Explanation:**

**Example 2:**

**Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]

**Output:** [4,6,7,5,2,9,8,3,1]

**Explanation:**

**Example 3:**

**Input:** root = []

**Output:** []

**Example 4:**

**Input:** root = [1]

**Output:** [1]

 

**Constraints:**

	- The number of the nodes in the tree is in the range `[0, 100]`.

	- `-100 <= Node.val <= 100`

 

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Solutions

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def post(root):
            if root is not None:
                post(root.left)
                post(root.right)
                res.append(root.val)
        post(root)
        return res
```
