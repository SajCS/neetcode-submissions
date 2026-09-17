# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []


        def bt(root, path):

            if not root:
                return False

            path.append(root.val)

            if not root.left and not root.right:
                found = sum(path) == targetSum
                path.pop()
                return found
            
            if bt(root.left, path) or bt(root.right, path):
                path.pop()
                return True
            path.pop()

            return False


        return bt(root, path)