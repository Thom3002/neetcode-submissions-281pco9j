"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # 1. percorre os neighbors do node se não tiverem no hashmap, adiciona. Pega o proximo index e pesquisa no hashmap, se não achar retorna. 

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy

        return dfs(node) if node else None

        
        
