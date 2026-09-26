class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        table = {}

        for k,v in knowledge:

            table[k] = v
        
        N = len(s)
        res = ""
        i = 0
        while i<N:
            
            if s[i]=="(":
                j = i+1
                key = ""
                while s[j]!=")":

                    key+=s[j]
                    j+=1

                i = j
                if key in table:
                    val = table[key]
                else:
                    val = "?"
            
                res += val

            else:
                res += s[i]
            i+=1
        
        return res