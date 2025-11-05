from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)
        sorted_numbers=sorted(frequency.items(),key=lambda x:x[1] ,reverse=True)
        result = []
        for item in sorted_numbers[:k]:
            result.append(item[0])
        return result