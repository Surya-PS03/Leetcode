# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        
        inorder_index = {val:i for i,val in enumerate(inorder)}

        idx = 0

        def buildTree(left,right):

            nonlocal idx

            if left>right:
                return

            rootVal = preorder[idx]
            idx+=1

            root = TreeNode(rootVal)

            mid = inorder_index[rootVal]

            root.left = buildTree(left,mid-1)
            root.right = buildTree(mid+1,right)

            return root
        
        N = len(preorder)
        return buildTree(0,N-1)
            
