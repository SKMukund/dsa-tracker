# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0
        
        self.max_val = root.val

        def dfs(node, val):
            if not node:
                return val
            
            left = dfs(node.left, val)
            right = dfs(node.right, val)

            left = max(left, 0)
            right = max(right, 0)
            
            val = val + node.val 
            
            self.max_val = max(self.max_val, left + right + node.val)

            return node.val + max(left,right)
        
        dfs(root, 0)

        return self.max_val
            

        