class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        even = (n+1)//2
        odd = n//2
        MOD = 10**9 + 7
        return (pow(5,even,MOD) * pow(4,odd,MOD)) % MOD