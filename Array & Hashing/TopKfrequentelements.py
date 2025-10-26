from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count numbers in the "nums"
        freq=Counter(nums)
        #sort the counts of numbers in "Descending order"
        #x[1] cause we are sorting by frequency not number 
        sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for item in sorted_items[:k]:
            #append the number not it's frequency
            result.append(item[0])
        return result