# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr=0

        def maxD(root)->int:
            if not root:
                return 0
            left=maxD(root.left)
            right=maxD(root.right)
            return 1+max(left,right) 
        
        return maxD(root)


            
         

               


        

        