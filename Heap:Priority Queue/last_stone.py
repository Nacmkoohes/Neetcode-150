import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]  # Max-heap with negative numbers
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest= heapq.heappop(stones)
            if largest != second_largest:
                heapq.heappush(stones, largest - second_largest)
        
        return -stones[0] if stones else 0
