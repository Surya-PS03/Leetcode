class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        N = len(seq)
        res = [0]*N
        depth = 0

        for i,pr in enumerate(seq):

            if pr == "(":
                res[i] = depth%2
                depth += 1
            elif pr==")":
                depth-=1
                res[i] = depth%2
        
        return res