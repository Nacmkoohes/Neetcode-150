class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        counts = [0] * 26 

        for r in range(len(s)):
            # Count the character at index r
            counts [ord(s[r]) - 65]+=1
            # Check if the current window is valid
            # If the number of characters that need to be replaced exceeds k, shrink the window
            # by moving the left pointer l to the right
            # The condition checks if the total length of the window minus the count of the most frequent
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest