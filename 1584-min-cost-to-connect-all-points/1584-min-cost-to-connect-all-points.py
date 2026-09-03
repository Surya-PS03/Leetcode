import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # compress the cordinates to node

        N = len(points)

        adj = [[] for _ in range(N)]

        for i in range(N-1):

            for j in range(i+1,N):

                manhattanDist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])

                adj[i].append((manhattanDist,j))
                adj[j].append((manhattanDist,i))

        
        # apply prims after creating adj list

        heap = [(0,0)]

        heapq.heapify(heap)

        visited = [0]*N

        cost = 0
        edges = 0

        while heap and edges<N:

            dist,curr = heapq.heappop(heap)

            if visited[curr]:
                continue
            
            visited[curr] = 1
            cost+=dist
            edges +=1

            for d,k in adj[curr]:
                heapq.heappush(heap,(d,k))

        return cost