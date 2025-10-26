class Solution(object):
    def maxArea(self, height):
        l=0
        n=len(height)
        r=n-1
        max_area=0
        while l<r:
            max_area=max(max_area,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area