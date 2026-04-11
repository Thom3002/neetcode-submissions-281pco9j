# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If p > n > q: n is ancestor
        # if p >= n >= q: n is ancestor
        # else proximo node
        # 1 5 6 entre -> é LCA
        # 5 5 6 entre ou igual
        # 7 5 9 ambos maiores
        # 1 5 2 ambos menores
        # 5 5 5 todos iguais -> é LCA

        visited = set()
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_node = queue.popleft()
            if curr_node not in visited:
                if p.val >= curr_node.val >= q.val or q.val >= curr_node.val >= p.val:
                    return curr_node
                
                elif p.val > curr_node.val and q.val > curr_node.val:
                    if curr_node.right:
                        queue.append(curr_node.right)
                
                else:
                    if curr_node.left:
                        queue.append(curr_node.left)
                
                visited.add(curr_node)
        
        return root
            
                    