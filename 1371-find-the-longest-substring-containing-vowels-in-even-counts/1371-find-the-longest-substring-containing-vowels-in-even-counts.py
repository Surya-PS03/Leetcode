class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        mask = 0
        state = {mask:-1}
        
        N = len(s)
        res = 0
        for i,char in enumerate(s):
            
            if char=="a":
                mask = mask ^(1<<0)
            elif char=="e":
                mask = mask ^ (1<<1)
            elif char=="i":
                mask = mask ^ (1<<2)

            elif char=="o":
                mask = mask ^ (1<<3)

            elif char=="u":
                mask = mask ^ (1<<4)
            
            if mask in state:
                res = max(res,i-state[mask])
            else:
                state[mask] = i

        return res
