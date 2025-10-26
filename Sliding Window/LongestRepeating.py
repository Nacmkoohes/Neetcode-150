class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        n=len(s)
        l=0
        counts=[0]*26
        for r in range(n):
            counts[ord(s[r])-65]+=1
            window=r-l+1
            #when things that needs to be changes are more than k
            while window - max(counts)>k:
                counts[ord(s[l])-65] -=1
                l+=1
                window=r-l+1
            longest=max(longest,window)
        return longest

