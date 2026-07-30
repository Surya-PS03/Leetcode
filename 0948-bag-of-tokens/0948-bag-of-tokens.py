class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens = sorted(tokens)
        N = len(tokens)

        if N==0 or power<tokens[0]:
            return 0
        
        i = 0
        j = N-1
        score = 0 
        finalScore = 0

        while i<=j:

            if power<tokens[i]:
                power += tokens[j]
                score -=1
                j-=1
            else:
                power-=tokens[i]
                i+=1
                score+=1
            finalScore = max(score,finalScore)
        return finalScore
        