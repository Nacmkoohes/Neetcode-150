class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res







