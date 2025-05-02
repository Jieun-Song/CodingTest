# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.deep = 0
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.down(root,0)
        return self.deep

    def down(self, root: Optional[TreeNode], num:int) -> int:
        num += 1
        if root.left:
            self.down(root.left, num)
        if root.right:
            self.down(root.right, num)
        if self.deep < num:
            self.deep = num
        return num   
