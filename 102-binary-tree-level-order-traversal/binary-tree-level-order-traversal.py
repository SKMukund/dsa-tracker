# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level = []
            height = len(queue)

            for _ in range(height):
                node = queue.popleft()
                level.append(node.val)

                left = node.left
                right = node.right

                if node.left:
                    queue.append(left)
                
                if node.right:
                    queue.append(right)

            result.append(level)
        return result
        