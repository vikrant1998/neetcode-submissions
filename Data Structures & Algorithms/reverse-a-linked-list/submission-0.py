# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        nodePtr = head
        prev, next = None, None

        while nodePtr != None:
            next = nodePtr.next
            nodePtr.next = prev
            prev = nodePtr
            nodePtr = next

        return prev