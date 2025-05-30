# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        prev = None
        while now:
            temp = now.next
            now.next = prev
            prev = now
            now = temp
        return prev