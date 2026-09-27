class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        N = len(s)
        st = []

        for i in range(N):

            if s[i] == ")":
                sample = []
                
                while st[-1] != "(":
                    sample.append(st.pop())
                
                st.pop()

                st.extend(sample)
            
            else:
                st.append(s[i])


        return "".join(st)




