class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # range according to test case 1 [1,12] -> count(0,12)-count(0,1-1)
        # if sum of digits reaches between min_sum and max_sum return 
        MOD = 10**9 +7
        def count(N):
            
            
            digits = [int(c) for c in N]
            dp = [[-1]*(9*len(digits)) for _ in range(len(N))]

            def helper(idx,tight,curr_sum):

                if idx==len(digits):

                    return 1 if (curr_sum >= min_sum and curr_sum <= max_sum) else 0
                
                if not tight and dp[idx][curr_sum]!=-1:
                    return dp[idx][curr_sum]
                
                ans = 0
                limit = digits[idx] if tight else 9

                for d in range(limit+1):

                    next_tight = tight and (d==limit)

                    ans += (helper(idx+1,next_tight,curr_sum+d)%MOD)


                if not tight:
                    dp[idx][curr_sum] = ans%MOD
                
                return ans


            return helper(0,1,0)
        

        left = count(num1)
        right = count(num2)
        
        x = sum(int(c) for c in num1)
        valid_num1 = 1 if (x>=min_sum and x<=max_sum) else 0

        return (right-left+valid_num1)%MOD