# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1

        nodePtr1 = list1
        nodePtr2 = list2
        head, tail = None, None
        nodePtr = None

        while nodePtr1 and nodePtr2:
            if head == None:
                head = ListNode()
                tail = head
                nodePtr = head
            else:
                nodePtr = ListNode()
                tail.next = nodePtr
                tail = nodePtr
            
            if nodePtr1.val < nodePtr2.val:
                tail.val = nodePtr1.val
                nodePtr1 = nodePtr1.next
            elif nodePtr1.val > nodePtr2.val:
                tail.val = nodePtr2.val
                nodePtr2 = nodePtr2.next
            else:
                tail.val = nodePtr1.val
                nextNode = ListNode(nodePtr2.val)
                tail.next = nextNode
                tail = nextNode
                nodePtr1 = nodePtr1.next
                nodePtr2 = nodePtr2.next

        while nodePtr1 != None:
            node = ListNode(nodePtr1.val)
            tail.next = node
            tail = node
            nodePtr1 = nodePtr1.next

        while nodePtr2 != None:
            node = ListNode(nodePtr2.val)
            tail.next = node
            tail = node
            nodePtr2 = nodePtr2.next

        return head
        