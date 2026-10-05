class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        score = 0
        st = []
        N = len(s)

        for i in range(N):

            if s[i] == "(":
                st.append(score)
                score = 0
            else:

                if s[i-1] == "(":
                    score = st[-1] + 1
                else:
                    score = st[-1] + (2*score)

                st.pop()
        
        return score
