from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        # i,j move in DP from left and right and end
        # turn variable to keep an account of who will pick next number
        # player 1 add it and player 2 subtracts it 

        # states i,j,turn
        N = len(nums)
        @cache
        def solve(i,j,turn,total):

            if i>j:
                return total

            if turn:
                total = max(nums[i]+solve(i+1,j,0,total+nums[i]),
                nums[j]+solve(i,j-1,0,total+nums[j]))
            else:
                total = min(-nums[i]+solve(i+1,j,1,total-nums[i]),
                -nums[j]+solve(i,j-1,1,total-nums[j]))
            

            return total

        return True if solve(0,N-1,1,0)>=0 else False