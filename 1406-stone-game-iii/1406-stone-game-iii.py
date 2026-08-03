from functools import cache
class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        
        # 3 choices pick 1, or 12 or 123

        N = len(nums)

        @cache
        def solve(i):

            if i>=N:
                return 0
            
            x = nums[i]-solve(i+1)
            y = float("-inf")
            if i+1<N:
                y = sum(nums[i:i+2])-solve(i+2)
            z = float("-inf")
            if i+2<N:
                z = sum(nums[i:i+3])-solve(i+3)
            
            return max(x,y,z)
        

        diff = solve(0)

        if diff>0: return "Alice"
        elif diff==0: return "Tie"
        else: return "Bob"