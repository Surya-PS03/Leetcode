class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        count = 0
        ans = ""
        i = 0
        j = 0
        N = len(s)

        while j < N:

            if s[j] == "1":
                count+=1

            # leading zeros ko bhi hatana hai unnecessary length nhi badhani
            while count > k or (i<=j and s[i]=="0" and count==k):

                if s[i] == "1":
                    count-=1
                i+=1


            if count == k:

                cand = s[i:j+1]

                # if empty make ans, candidate has smaller length, if same length check lexicographically
                if not ans or len(cand)<len(ans) or (len(cand)==len(ans) and cand<ans):
                    ans = cand
            j+=1
        return ans