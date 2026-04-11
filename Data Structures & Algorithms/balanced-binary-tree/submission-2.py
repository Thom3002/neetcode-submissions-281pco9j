# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs in left and right count depth and then compare for each call 
        def dfs(node):
            if node == None:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = (left[0] and right[0] and abs(right[1] - left[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])] 

        return dfs(root)[0]