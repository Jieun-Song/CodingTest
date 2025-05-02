# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.floor = {}
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root:
            self.down(root,1)
            for key in self.floor.keys():
                self.floor[key] = sum(self.floor[key])
            for key in self.floor.keys():
                if self.floor[key] == max(list(self.floor.values())):
                    return key
    def down(self, root:Optional[TreeNode], num:int):
        if num in self.floor.keys():
            self.floor[num].append(root.val)
        else:
            self.floor[num] = [root.val]
        if root.left:
            self.down(root.left, num+1)
        if root.right:
            self.down(root.right, num+1)
        