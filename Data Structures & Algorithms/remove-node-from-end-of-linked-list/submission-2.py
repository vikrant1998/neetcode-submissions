# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodePtr = head
        count = n
        while nodePtr and count > 0:
            nodePtr = nodePtr.next
            count -= 1

        nodeFirst = head
        prev = None
        while nodePtr:
            prev = nodeFirst
            nodeFirst = nodeFirst.next
            nodePtr = nodePtr.next

        if prev:
            prev.next = nodeFirst.next
        else:
            return head.next
        del nodeFirst
        return head

        