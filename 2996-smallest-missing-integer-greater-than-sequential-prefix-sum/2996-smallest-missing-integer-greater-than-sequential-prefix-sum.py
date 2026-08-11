class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        s = set(nums)

        curr_sum = nums[0]
        glob_sum = nums[0]
        
        N = len(nums)

        for i in range(1,N):

            if nums[i] == nums[i-1]+1:
                curr_sum += nums[i]
                glob_sum = max(glob_sum,curr_sum)
            else:
                break

        print(s)
        if glob_sum not in s:
            return  glob_sum
        else:
            u = glob_sum+1

            while u in s:
                u+=1
            
            return u