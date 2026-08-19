from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
         
        mask = defaultdict(int)

        chars = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

        for word in words:

            for char in word:

                mask[word] = mask[word] | (1<<chars[char])
        
        N = len(words)
        maxLen = 0
        for i in range(N-1):
            for j in range(i+1,N):
                
                mask1 = mask[words[i]]
                mask2 = mask[words[j]]
                
                if mask1 & mask2 == 0:
                    maxLen = max(maxLen,len(words[i])*len(words[j]))
        
        return maxLen
