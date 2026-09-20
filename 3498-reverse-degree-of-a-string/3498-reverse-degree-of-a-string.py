class Solution:
    def reverseDegree(self, s: str) -> int:
        
        sum = 0
        for i,char in enumerate(s):

            prod = (i+1) * (26 - (ord(char)-97))

            sum += prod
        
        return sum