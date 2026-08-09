# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []
        def dfs(node, val, path):

            if not node:
                return
            
            val = val + node.val
            path.append(node.val)
            
            if val == targetSum and not node.left and not node.right:
                result.append(path[:])

            dfs(node.left, val, path)
            dfs(node.right, val, path)

            path.pop()
        
        dfs(root, 0, [])
        
        return result
        