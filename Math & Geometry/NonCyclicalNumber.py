class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ^ 2 for digit in str(n))
               
# If n becomes 1, it means the number is happy (non-cyclical), so return True.
# If we exit the loop because we saw the same number again, it means we're in a loop, so return False.
# This line checks which of those two cases happened.
        return n == 1
