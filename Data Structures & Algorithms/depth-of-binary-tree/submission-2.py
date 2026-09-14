from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = deque()
        depth = 0
        highestDepth = 0
        if root:
            depth += 1
            stack.append((root, depth))

        while stack:
            curr = stack.popleft()
            if curr[1] > highestDepth:
                highestDepth = curr[1]
            if curr[0].left:
                stack.append((curr[0].left, curr[1]+ 1))
            if curr[0].right:
                stack.append((curr[0].right, curr[1]+ 1))
        return highestDepth
        
    
        
        