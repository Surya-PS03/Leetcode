class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1]*n
        st = []
        for i in range(2*n):

            while st and nums[st[-1]]<nums[i%n]:
                pop_idx = st.pop()
                ans[pop_idx] = nums[i%n]
            
            if i<n:
                st.append(i)
        
        return ans

