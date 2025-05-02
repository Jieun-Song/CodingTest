# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        now = head
        for _ in range(length//2):
                now = now.next
            
        return now
        