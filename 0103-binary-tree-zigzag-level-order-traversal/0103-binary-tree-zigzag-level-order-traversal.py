# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        if root == None:
            return res
        q = deque([])

        q.append(root)

        # status for keeping track to trverse in forward or backward depending of level
        status = 0

        while q:
            
            l = len(q)
            level = [0]*l

            for i in range(l):
                node = q.popleft()

                index = l-i-1 if status else i

                level[index] = node.val


                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            status = not status
            res.append(level)
        
        return res
            




            