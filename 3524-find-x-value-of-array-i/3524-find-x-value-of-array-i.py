
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        
        prev = [0]*k
        ans = [0]*k

        for num in nums:
            new = [0]*k
            new[num%k]+=1 #add current number to remainder count
            for r in range(k):
                idx = (r*num)%k
                new[idx] += prev[r]
            prev = new

            for r in range(k):

                ans[r] += new[r]
        
        return ans


           