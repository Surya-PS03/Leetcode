from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # i,j pointer increment j if you encounter freq[nums[j]]>k then:
            # create a while loop until you until freq[nums[j]]!=k, increment i and decrement all freq[nums[i]]-=1
        # with every j iteration and frequency increment chech max(maxLen,j-i+1)

        i,j = 0,0
        N = len(nums)
        freq = defaultdict(int)
        maxLen = 0

        while j<N:

            freq[nums[j]]+=1

            while freq[nums[j]]>k:

                freq[nums[i]]-=1
                i+=1

            maxLen = max(maxLen,j-i+1)

            j+=1
        
        return maxLen

