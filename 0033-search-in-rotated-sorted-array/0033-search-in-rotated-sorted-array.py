class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        n = len(nums)
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if nums[mid]==target:
                return mid
            
            if nums[low]<=nums[mid]:
                if nums[low]<=target and nums[mid]>=target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target and nums[high]>=target:
                    low = mid+1
                else:
                    high = mid-1
        return -1

