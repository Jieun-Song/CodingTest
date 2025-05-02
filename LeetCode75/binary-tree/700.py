# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            self.down(root, val)
            return self.found
        else:
            return False
        
    def down(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            self.found = root
        elif root.val > val:
            self.down(root.left, val)
        elif root.val < val:
            self.down(root.right, val)