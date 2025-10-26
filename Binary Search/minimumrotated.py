class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<r:
            mid=(l+r)//2
            # Check if mid is greater than the last element
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        # At the end of the loop, l will point to the smallest element
        return nums[l]  