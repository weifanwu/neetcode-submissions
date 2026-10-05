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
        nodes_match = {None : None}
        current = head
        while current:
            nodes_match[current] = Node(current.val)
            current = current.next
        current = head
        
        while current:
            nodes_match[current].next = nodes_match[current.next]
            nodes_match[current].random = nodes_match[current.random]
            current = current.next

        return nodes_match[head]


