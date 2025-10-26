class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       #m is rows, n is columns
        m=len(matrix)
        n=len(matrix[0])
        t=m*n
        l=0
        r=t-1
        while l<=r:
            mid=(l+r)//2
            i=mid//n
            j=mid%n
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                l=mid+1
            else:
                r=mid-1
        return False