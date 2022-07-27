# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        res = []
        level = 0
        queue.append(root)
        while(len(queue) > 0):
            tmp = []
            for i in range(len(queue)):
                node = queue[0]
                tmp.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                queue.popleft()
            if(level % 2 == 0):
                tmp.reverse()
            res.append(tmp)
            level += 1
        
        return res
