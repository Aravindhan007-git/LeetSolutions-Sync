# Binary Tree Inorder Traversal

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-tree-inorder-traversal` |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Solved | 2026-09-18 |
| Solve Time | 35m 58s |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.2 MB (beats 92.6312%) |

## Problem Statement

Given the `root` of a binary tree, return _the inorder traversal of its nodes' values_.

 

**Example 1:**

**Input:** root = [1,null,2,3]

**Output:** [1,3,2]

**Explanation:**

**Example 2:**

**Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]

**Output:** [4,2,6,5,7,1,3,9,8]

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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def inorder(root):
            if root is not None:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res

```
