class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        palindrome = [[0]*N for _ in range(N)]

        count = 0
        for end in range(N):
            for start in range(end+1):
                if s[start]==s[end]:
                    if end-start<=2 or palindrome[start+1][end-1]:
                        palindrome[start][end] = 1
                        count+=1
        
        return count