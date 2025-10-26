class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            #midpoint calculation and l+(r-l)//2 to avoid overflow
            m=l+(r-l)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        return -1
       

            
