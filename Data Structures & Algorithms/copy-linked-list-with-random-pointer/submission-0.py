"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idxMap = dict()
        i = 0

        nodePtr = head
        while nodePtr:
            idxMap[nodePtr] = Node(nodePtr.val)
            nodePtr = nodePtr.next
        idxMap[None] = None

        nodePtr = head
        headF = None
        while nodePtr:
            currNode = idxMap[nodePtr]
            nextNode = idxMap[nodePtr.next]
            randNode = idxMap[nodePtr.random]
            currNode.next = nextNode
            currNode.random = randNode
            if headF == None:
                headF = currNode
            nodePtr = nodePtr.next

        return headF
