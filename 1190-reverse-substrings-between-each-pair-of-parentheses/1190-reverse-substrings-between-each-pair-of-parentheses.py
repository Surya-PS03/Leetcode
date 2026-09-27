class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        N = len(s)
        st = []

        for i in range(N):

            if s[i] == ")":
                sample = ""
                
                while st[-1] != "(":
                    char = st.pop()
                    sample += char
                
                st.pop()

                for char in sample:
                    st.append(char)
            
            else:
                st.append(s[i])


        return "".join(st)




