# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. for every node in root check if is == subroot

        def is_equal(p, q):
            
            def dfs(p, q):
                if not p and not q:
                    return True
                elif not p or not q:
                    return False
                
                if p.val != q.val:
                    return False

                condition = dfs(p.left, q.left) and dfs(p.right, q.right)
                return condition

            return dfs(p, q)

        def bfs(node):
            visited = set()
            queue = collections.deque()
            queue.append(node)
            

            while queue:
                curr_node = queue.popleft()
                if curr_node == None:
                    break
                if curr_node not in visited:
                    if is_equal(curr_node, subRoot):
                        return True
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
                    visited.add(curr_node)

            return False
        
        return bfs(root)

