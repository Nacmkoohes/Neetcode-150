from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set is used to store unique elements
        seen=set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False