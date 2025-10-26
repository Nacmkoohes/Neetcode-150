import heapq
from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        freq = Counter(tasks)
        # how many times the most frequent task appears
        max_freq = max(freq.values())
        # Count how many tasks have the maximum frequency
        max_count = sum(1 for count in freq.values() if count == max_freq)
        #calculate the total time required
        total_time = (max_freq - 1) * (n + 1) + max_count
        # Return the maximum of total time and the length of tasks
        return max(total_time, len(tasks))
