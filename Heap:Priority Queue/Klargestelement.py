# #brute_force
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.nums=nums
#         self.k=k
#
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort(reverse=True)
#         # Note: To get the kth largest element, sort the list in descending order and return self.nums[k-1]
#         return self.nums[self.k-1]
from typing import List
import heapq

# heap solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


