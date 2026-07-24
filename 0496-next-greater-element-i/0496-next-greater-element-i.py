class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        ans = []
        loc = {}

        for i,num in enumerate(nums2):

            loc[num] = i

        for num in nums1:
            flag = 0
            for j in range(loc[num],len(nums2)):

                if nums2[j]>num:
                    ans.append(nums2[j])
                    flag=1
                    break
            
            if flag==0:
                ans.append(-1)
        
        return ans
            