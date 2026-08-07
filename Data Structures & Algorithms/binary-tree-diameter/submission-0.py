# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0

        def height(root)->int:
            if not root:
                return 0
           
            left=height(root.left)
            right=height(root.right)
            temp=left+right
            nonlocal dia
            dia=max(dia,temp)

            return max(left,right)+1
        
        height(root)
        return dia