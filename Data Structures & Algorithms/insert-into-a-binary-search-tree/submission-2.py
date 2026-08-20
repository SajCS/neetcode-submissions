# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            root = TreeNode(val)
            return root
        self.findNode(root,val)
        return root


    def findNode(self, root, val):
        if root != None:
            if root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    self.findNode(root.right, val)
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    self.findNode(root.left, val)
       





























    #     dummyRoot = TreeNode(0, left = root)
    #     foundRoot = self.findNode(root, val)
    #     foundRoot = TreeNode(val)
    #     print(dummyRoot.left, foundRoot)
    #     return dummyRoot.left
 
    


    # def findNode(self, root, val):

    #     if root != None:
    #         if root.val > val:
    #                 root = self.findNode(root.left, val)
    #         else:
    #             root = self.findNode(root.right,val)
    #     return root

        

        