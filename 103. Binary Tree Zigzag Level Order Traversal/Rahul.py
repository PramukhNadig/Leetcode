# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = [root]
            traversal = []
            level = 1
            while queue:
                oldQueue = queue
                queue = []
                
                traversal.append([])
                for node in oldQueue:
                    traversal[-1].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if level % 2 == 0:
                    traversal[-1].reverse()
                level += 1
                    
            return traversal
        else:
            return []
