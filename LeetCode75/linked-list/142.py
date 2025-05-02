# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            visited.add(curr) 
            curr = curr.next
        return None 