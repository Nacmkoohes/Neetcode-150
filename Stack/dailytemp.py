class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        n= len(temperatures)
        stack = []
        ans = [0] * n
        for i,t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
        # This function calculates the number of days until a warmer temperature for each day in the input

                 