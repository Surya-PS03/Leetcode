class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [""]

        for ch in s:
            # new substring found to be reversed
            if ch == "(":
                st.append("")
            # close the substring add it major/parent string
            elif ch == ")":
                temp = st.pop()[::-1]
                st[-1] += temp
            # casually add new character if no new substring found or no closing found
            else:
                st[-1] += ch
        
        return st[0]