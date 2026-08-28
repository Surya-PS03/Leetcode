class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        N  = len(s)

        # quick lookup table for palindrome
        palindrome = [[0]*N for _ in range(N)]

        for end in range(N):

            for start in range(end):

                if s[start] == s[end]:

                    if (end-start)<=2 or palindrome[start+1][end-1]:
                        palindrome[start][end] = 1

        maxPalindrome = 0
        maxi,maxj = 0,0
        for i in range(N):
            for j in range(N):

                if palindrome[i][j]:

                    if j-i+1 > maxPalindrome:
                        maxPalindrome = j-i+1
                        maxi,maxj = i,j

        res = ""
        for chari in range(maxi,maxj+1):

            res += s[chari]
        
        return res

