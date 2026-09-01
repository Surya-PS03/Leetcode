class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        
        N = len(nums)
        count = 0

        for i in range(N):
            countEven = 0
            countOdd = 0

            for j in range(i,N):

                if nums[j]&1==1:
                    countOdd+=1
                else:
                    countEven+=1
                
                if countOdd !=0 and countEven/countOdd <= a/b:
                    count+=1
        return count