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
        if not head:
            return None
        
        oldNewDict = {}
        curr = head
        while curr:
            oldNewDict[curr] = oldNewDict.get(curr, Node(curr.val))
            
            if curr.next:
                oldNewDict[curr].next = oldNewDict.get(curr.next, Node(curr.next.val))
                oldNewDict[curr.next] = oldNewDict[curr].next
                
            if curr.random:
                oldNewDict[curr].random = oldNewDict.get(curr.random, Node(curr.random.val))
                oldNewDict[curr.random] = oldNewDict[curr].random
                
            curr = curr.next
                    
        return oldNewDict[head]
