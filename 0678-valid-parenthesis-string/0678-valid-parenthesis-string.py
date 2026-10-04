class Solution:
    def checkValidString(self, s: str) -> bool:
        
        N = len(s)
        openBr = 0
        closeBr = 0
        for i in range(N):

            if s[i]=="(" or s[i]=="*":
                openBr+=1
            else:
                openBr-=1
            
            if openBr<0:
                return False
        
        for i in range(N-1,-1,-1):

            if s[i]==")" or s[i]=="*":
                closeBr+=1
            else:
                closeBr-=1
            
            if closeBr<0:
                return False
        
        return True