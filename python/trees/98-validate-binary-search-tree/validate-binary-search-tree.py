# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if not root:
            return False
        
        def dfs(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right
            
        
        return dfs(root, float("-inf"), float("inf"))
        