class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # Pair positions with speeds and sort by position in descending order
        # This allows us to process cars from the furthest position to the closest
        pairs = sorted(zip(position, speed), reverse=True)
        
        for pos, spd in pairs:
            # Calculate the time it takes for the current car to reach the target
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                # If the stack is empty or the current car takes longer than the last car in the stack,
                # it forms a new fleet
                
                stack.append(time)
        
        return len(stack)
        # This function calculates the number of car fleets that will reach the target. 