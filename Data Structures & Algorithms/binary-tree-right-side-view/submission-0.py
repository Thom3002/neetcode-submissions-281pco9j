# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            curr_max = 0
            for _ in range(len(q)): # iterates through each level 
                curr = q.popleft()
                if curr:
                    # get the max num
                    curr_max = max(curr_max, curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            res.append(curr_max)        

        return res
