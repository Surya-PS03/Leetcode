class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        
        def count(N):

            digits = [int(c) for c in N]
            
            L = len(digits)
            MAX_DIFF = 2*L+1
            
            dp = [
                [
                    [
                        [-1]*(k) for _ in range(MAX_DIFF)
                    ] for _ in range(2)
                ] for _ in range(L)
            ]


            def helper(idx,tight,is_zero,count,rem):

                if idx == len(digits):
                    if not is_zero:
                        return 1 if count==0 and rem==0 else 0
                    else:
                        return 0
                

                if not tight and dp[idx][is_zero][count+L][rem]!=-1:
                    return dp[idx][is_zero][count+L][rem]
                
                ans = 0

                limit = digits[idx] if tight else 9

                for d in range(limit+1):
                    
                    next_tight = tight and (d==limit)

                    next_zero = is_zero and (d==0)

                    new_rem = (rem*10+d)%k

                    next_count = count
                    if not next_zero:
                        next_count += 1 if d%2==0 else -1

                    ans += helper(idx+1,next_tight,next_zero,next_count,new_rem)

                
                if not tight:
                    dp[idx][is_zero][count+L][rem] = ans
                return ans


            return helper(0,1,1,0,0)
        

        left = count(str(low-1))
        right = count(str(high))

        return right-left