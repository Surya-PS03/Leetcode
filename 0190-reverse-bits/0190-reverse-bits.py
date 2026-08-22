class Solution:
    def reverseBits(self, n: int) -> int:
        
        for i in range(16):

            if not (n&(1<<i)) and (n&(1<<(31-i))):
            
                n = n & ~(1<<(31-i))
                n = n | (1<<i)
            
            elif n&(1<<i) and (not n&(1<<(31-i))):

                n = n & ~(1<<i)
                n = n | (1<<(31-i))
            
        return n