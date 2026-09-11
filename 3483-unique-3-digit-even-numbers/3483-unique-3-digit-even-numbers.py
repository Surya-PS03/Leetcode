class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        s = set()
        N = len(digits)
        for i in range(N):
            if digits[i]==0: continue

            for j in range(N):

                for k in range(N):

                    if i==j or i==k or k==j:
                        continue
                    
                    num = digits[i]*100 + digits[j]*10 + digits[k]

                    if num%2==0:
                        s.add(num)
        
        return len(s)
