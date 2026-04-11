# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_size = len(queue)
            level = []
            for i in range(queue_size):
                curr = queue.popleft()
                if not curr:
                    break

                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            res.append(level)
        
        return res
            

            
