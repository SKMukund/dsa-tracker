# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if not root:
            return None

        self.result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            self.result.append(node.val)

            dfs(node.right)

        dfs(root)

        return self.result[k - 1]
        
        