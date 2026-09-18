# Binary Tree Preorder Traversal

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-tree-preorder-traversal` |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Solved | 2026-09-18 |
| Solve Time | 35m 58s |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 69.01310000000001%) |

## Problem Statement

Given the `root` of a binary tree, return _the preorder traversal of its nodes' values_.

 

**Example 1:**

**Input:** root = [1,null,2,3]

**Output:** [1,2,3]

**Explanation:**

**Example 2:**

**Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]

**Output:** [1,2,4,5,6,7,3,8,9]

**Explanation:**

**Example 3:**

**Input:** root = []

**Output:** []

**Example 4:**

**Input:** root = [1]

**Output:** [1]

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 100]`.

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
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def preorder(root):
            if root is not None:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res
```
