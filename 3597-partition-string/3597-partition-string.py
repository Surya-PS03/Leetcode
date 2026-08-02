class Solution:
    def partitionString(self, s: str) -> List[str]:
        
        i = 0 
        j = 0
        N = len(s)
        occ = dict()
        segment = []
        while j<N and i<=j:
            
            segment.append(s[j])
            x = "".join(segment)
            if x not in occ:
                occ[x] = 0
                i = j+1
                segment = []
            
            j+=1
        

        return list(occ.keys())

