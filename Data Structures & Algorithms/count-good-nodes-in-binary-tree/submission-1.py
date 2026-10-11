# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, mVal):
            nonlocal count

            if not root:
                return 0
            
            if root.val >= mVal:
                count += 1
                mVal = root.val
            
            dfs(root.left, mVal)
            dfs(root.right, mVal)
        dfs(root, -1000)
        return count
        