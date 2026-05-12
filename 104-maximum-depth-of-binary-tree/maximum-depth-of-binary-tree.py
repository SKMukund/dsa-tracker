# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0

        def maxDepthHelper(node, count):
            if not node:
                return count
            return max(maxDepthHelper(node.left, count + 1), maxDepthHelper(node.right, count + 1))

        return maxDepthHelper(root, 0)
    
    
        