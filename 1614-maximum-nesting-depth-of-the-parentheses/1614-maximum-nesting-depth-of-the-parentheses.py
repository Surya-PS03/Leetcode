class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxDepth = 0
        curr = 0
        for char in s:

            if char == "(":
                curr+=1
            elif char==")":
                maxDepth = max(curr,maxDepth)
                curr-=1
        
        return maxDepth