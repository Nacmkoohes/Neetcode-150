class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        # Count frequency of characters in s1 and the first n1 characters of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True
        # Slide the window over s2
        for i in range(n1, n2):
            # Update the counts for the current window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the character that is sliding out of the window
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1
            # Check if the counts match
            if s1_count == s2_count:
                return True

        return False
