# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        head = None
        tail = None
        q = []
        for l in lists: heapq.heappush(q, HeapNode(l))

        while len(q) > 0:
            element = heapq.heappop(q)
            if element.node.next != None:
                heapq.heappush(q, HeapNode(element.node.next))
            if head == None:
                head = ListNode(element.node.val)
                tail = head
            else:
                tail.next = ListNode(element.node.val)
                tail = tail.next

        return head