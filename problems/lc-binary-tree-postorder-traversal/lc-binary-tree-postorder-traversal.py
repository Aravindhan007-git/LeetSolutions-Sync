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