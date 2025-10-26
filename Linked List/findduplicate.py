class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            #move slow by one step and fast by two steps
            slow = nums[slow]
            fast = nums[nums[fast]]
            #loop detected
            if slow == fast:
                break

        slow = nums[0]
        #find the entrance to the cycle
        while slow != fast:

            slow = nums[slow]
            fast = nums[fast]
        #the duplicate number is the entrance to the cycle
    

        return slow
