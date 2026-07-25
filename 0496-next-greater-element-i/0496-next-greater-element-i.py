class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hmap = {}

        st = []
        st.append(nums2[0])

        for i in range(1,len(nums2)):
            val = nums2[i]
            
            if st[-1]>val:
                st.append(val)
                continue
            else:
                while st and st[-1]<val:
                    hmap[st[-1]] = val
                    st.pop()
                
                st.append(val)
        
        if st:
            while st:
                hmap[st[-1]] = -1
                st.pop()
        print(hmap)
        ans = []
        for num in nums1:   
            ans.append(hmap[num])
        
        return ans