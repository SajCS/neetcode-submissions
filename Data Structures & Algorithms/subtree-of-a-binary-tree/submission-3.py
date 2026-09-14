# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Find the subroot within the root
        #SameTree


        def findSubroot(root):
            if not root:
                return False

            #Preorder traversal
            print(root.val , subRoot.val)
            if root.val == subRoot.val and isSame(root, subRoot):
                return True
                
            return findSubroot(root.left) or findSubroot(root.right)
        
        def isSame(root, subroot):
            if not root and not subroot:
                return True
            elif root and not subroot:
                return False
            elif not root and subroot:
                return False
            elif root.val != subroot.val:
                return False
            else:
                return isSame(root.left, subroot.left) and isSame(root.right, subroot.right)
        
        return findSubroot(root)

        
        