class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        #hashmap to keep track if  the difference is in seen
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[num] = i