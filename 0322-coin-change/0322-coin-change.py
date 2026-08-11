class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # choices at each step = len(coins)
        # if amount == 0 return 1
        # if amount < 0 return 0
        dp = [-1]*(amount+1)

        def solve(A):

            if A==0:
                return 0
            elif A<0:
                return float("inf")

            if dp[A] !=-1:
                return dp[A]
            # choices
            min_coins = float("inf")
            for i in range(len(coins)):
                x = 1+solve(A-coins[i])
                min_coins = min(min_coins,x)

            dp[A] = min_coins
            return dp[A]

        ans = solve(amount)
        return -1 if ans==float("inf") else ans