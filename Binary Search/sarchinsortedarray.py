from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= en(nums)
        l=0
        r=n-1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half must be sorted
            else:#(nums[l]> nums[mid]):
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
