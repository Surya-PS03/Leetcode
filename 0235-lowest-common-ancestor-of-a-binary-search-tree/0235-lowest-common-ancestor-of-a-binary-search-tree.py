# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        


        def traverse(root):

            if root:
                if root==p:
                    return p
                elif root==q:
                    return q

                left = traverse(root.left)
                right = traverse(root.right)

                if left and right:
                    return root
                elif left and not right:
                    return left
                else:
                    return right
        
        return traverse(root)