from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
                        #we have two choices: take one stair or two stairs
                        #if we take one stair, we add cost[i-1] to dp[i-1] and if we take two stairs, we add cost[i-2] to dp[i-2]
        return dp[n]