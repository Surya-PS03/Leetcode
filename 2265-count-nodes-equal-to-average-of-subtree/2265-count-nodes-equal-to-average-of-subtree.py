# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        # instead of calculating average and returning it return sum and counts and ans from that node

        def solve(root):

            if root == None:
                return 0,0,0
            

            left, leftCount, leftAns = solve(root.left)
            right, rightCount, rightAns = solve(root.right)


            totalSum = left + right + root.val
            totalCount = 1 + leftCount + rightCount

            avg = totalSum // totalCount

            ans = leftAns + rightAns

            if avg == root.val:
                ans+=1


            return totalSum, totalCount, ans
        

        _, __, ans = solve(root)

        return ans