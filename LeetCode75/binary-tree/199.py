# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.floor = {}
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.down(root,1)
        print(self.floor)
        result = []

        for key in self.floor.keys():
            result.append(max(self.floor[key]))
        return result

    def down(self, root: Optional[TreeNode], num:int):
        if num in self.floor:
            self.floor[num].append(root.val)
        else:
            self.floor[num] = [root.val]
        if root.left:
            self.down(root.left, num+1)
        if root.right:
            self.down(root.right, num+1)