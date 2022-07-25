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
        random = {}
        
        curr = head
        dummy = Node(0)
        tmp = dummy
        while curr != None:
            dummy.next = Node(curr.val)
            random[curr] =  dummy.next
            dummy = dummy.next
            curr = curr.next
        curr = head
        dummy = tmp
        while dummy.next != None:
            dummy.next.random = random.get(curr.random, None)
            dummy = dummy.next
            curr = curr.next
        return tmp.next
