
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1
        majority = nums[0]
        N = len(nums)

        for i in range(1,N):
            
            if majority == nums[i]:
                count += 1
            else:
                count -=1

                if count == 0:
                    majority = nums[i]
                    count = 1

        return majority
        