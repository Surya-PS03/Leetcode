from collections import deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(n)]

        for u,v in invocations:
            adj[u].append(v)

        
        def dfs(node,visited=None):

            if visited==None:
                visited = set()
            
            visited.add(node)

            for newNode in adj[node]:
                if newNode not in visited:
                    dfs(newNode,visited)

            return visited

        infected = dfs(k)     

        for u,v in invocations:

            if u not in infected and v in infected:
                return list(range(n))
        
        return [i for i in range(n) if i not in infected]

        

        
        
       


            
            
