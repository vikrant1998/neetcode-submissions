# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        count = 0

        while fast != None:
            count += 1
            if fast.next == None:
                return False
            if slow == fast and count != 1:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
        