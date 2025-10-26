# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:#make sure we have fast.next so we can have fast= fast.next.next
            fast=fast.next.next# fast makes 2 step for 1 step of slow so when they become on one same node we have cycle
            slow=slow.next
            if fast is slow:
                return True
        return False
