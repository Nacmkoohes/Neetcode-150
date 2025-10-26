class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        char_set=set()
        n=len(s)
        for r in range(n):
           # Check if the character at index r is already in the set
            while s[r] in char_set:
                # If it is, remove the character at index l from the set
                char_set.remove(s[l])
                l += 1
            w=(r-l)+1
            longest=max(longest,w)
            char_set.add(s[r])
        return longest
            
