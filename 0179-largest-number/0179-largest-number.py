from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def cmp(a,b):
            if int(a+b)<int(b+a):
                return 1
            elif int(a+b)>int(b+a):
                return -1
            return 0
        
        nums = [str(num) for num in nums]

        nums.sort(key = cmp_to_key(cmp))
        
        ans = "".join(nums)

        if ans[0]=="0": return "0"

        return ans