class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        # subarray with maximum length whose sum = sum(arr) - x
        N = len(nums)
        target = sum(nums) - x

        if target == 0:
            return N

        i = 0
        j = 0
 
        resLen = 0
        currSum = 0

        while j<N:

            currSum += nums[j]
            
            while i<=j and currSum>target:
                currSum -= nums[i]
                i+=1

            if currSum == target:
                resLen = max(resLen,j-i+1)

            j+=1
        

        if resLen == 0:
            return -1
        
        return N-resLen