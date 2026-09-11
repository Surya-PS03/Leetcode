class Solution:
    def countBits(self, n: int) -> List[int]:
        

        # use brian kernighan's algorithm

        # it used to count number of set bits in a number in its binary representation

        res = []

        # number of times you remove LSB set bit the answer is that count
        for i in range(0,n+1):
            count = 0
            while i!=0:

                i = i & (i-1)  # it removes the righmost set bit (LSB with set bit)

                count+=1

            res.append(count)
        
        return res
