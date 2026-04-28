class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        # premap = {4: [0,1,2,3], 5: [4]}
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if premap[crs] == []:
                return True
            
            visited.add(crs)
            for c in premap[crs]:
                if not dfs(c): return False
            
            visited.remove(crs)
            premap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
