from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        # i,j move in DP from left and right and end
        # turn variable to keep an account of who will pick next number
        # player 1 add it and player 2 subtracts it 

        # states i,j,turn
        N = len(nums)
        @cache
        def solve(i,j):

            if i==j:
                return nums[i]

            left = nums[i]-solve(i+1,j)
            right = nums[j]-solve(i,j-1)
            

            return max(left,right)

        return solve(0,N-1)>=0