class Solution(object):
    def containsDuplicate(self, nums):
        char_set=set()
        for num in nums:
            if num in char_set:
                return True
            else:
                char_set.add(num)
        return False