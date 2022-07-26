# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tmp = root
        pSearch, qSearch = root, root
        while(pSearch == qSearch):
            tmp = qSearch
            if(pSearch == p):
                return p
            if(qSearch == q):
                return q
            if(pSearch.val > p.val):
                pSearch = pSearch.right
            else:
                pSearch = pSearch.left
            if(qSearch.val > q.val):
                qSearch = qSearch.right
            else:
                qSearch = qSearch.left
            
        return tmp
