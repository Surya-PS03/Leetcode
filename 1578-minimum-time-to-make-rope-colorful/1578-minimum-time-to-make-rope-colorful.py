class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # i,j pointer i=0 j=1 if colors[i]=colors[j] find minimum of them if i< then i+=1 j+=1, if j< then j+=1 but i remains still, if len(colors) <=1 return 0

        N = len(colors)
        if N<=1:
            return 0

        i = 0
        j = 1
        totalTime = 0

        while j<N:

            if colors[i]==colors[j]:
                if neededTime[i]<neededTime[j]:
                    totalTime += neededTime[i]
                    i = j
                    j += 1
                else:
                    totalTime += neededTime[j]
                    j+=1
            else:
                i = j
                j += 1

        return totalTime

