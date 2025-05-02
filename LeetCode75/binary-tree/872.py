# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.down(1,root1)
        self.down(2,root2)
        if self.arr1 == self.arr2:
            return True
        else:
            return False

    def down(self, num:int, root:Optional[TreeNode]) -> list:
        if root.left:
            self.down(num, root.left)
        if root.right:
            self.down(num, root.right)
        if root.left == None and root.right == None:
            if num == 1:
                self.arr1.append(root.val)
            if num == 2:
                self.arr2.append(root.val)