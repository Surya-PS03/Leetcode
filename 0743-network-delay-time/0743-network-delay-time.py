import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distances = {node:float("inf") for node in range(1,n+1)}

        adj = [[] for _ in range(n+1)]

        for u,v,w in times:
            adj[u].append((v,w))
        

        distances[k] = 0
        pq = [(0,k)]

        while pq:

            curr_dist,u = heapq.heappop(pq)

            # skip the longer time
            if curr_dist>distances[u]:
                continue

            
            for v,w in adj[u]:

                dist = curr_dist+w

                if distances[v]>dist:
                    distances[v] = dist
                    heapq.heappush(pq,(dist,v))
        
        max_time = max(distances.values()) #important 

        return max_time if max_time!=float("inf") else -1