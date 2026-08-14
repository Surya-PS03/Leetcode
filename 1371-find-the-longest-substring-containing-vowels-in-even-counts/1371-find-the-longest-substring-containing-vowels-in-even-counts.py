class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        state = {"00000":-1}
        
        N = len(s)

        stateList = {"a":0,"e":0,"i":0,"o":0,"u":0}
        res = 0
        for i in range(N):
            char = s[i]

            if char in stateList:
                stateList[char] = (stateList[char]+1)%2
                
            st = "".join(str(v)for v in stateList.values())

            if  st not in state:
                state[st] = i
            else:
                res = max(res, i-state[st])
        return res
