# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node):
            if not node:
                return 0

            leftHeight = helper(node.left)
            rightHeight = helper(node.right)

            if leftHeight == -1:
                return -1

            if rightHeight == -1:
                return -1

            if abs(leftHeight- rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)
        
        return helper(root) != -1
        
            


        