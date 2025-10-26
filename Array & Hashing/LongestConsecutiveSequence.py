class Solution(object):
    def longestConsecutive(self, nums):
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                next_num=num+1
                length=1
                while next_num in num_set:
                    next_num+=1
                    length+=1
                longest=max(longest,length)
        return longest