class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:

        if n==k:
            return 0
        
        components = n
        edges = sorted(edges,key=lambda x: x[2])


        parent = list(range(n))
        rank = [0]*n
        
        def find(x):

            while parent[x] != x:

                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return parent[x]
        
        # no rank needed here 
        # since edges sorted on basis of weight so no we will get all possible smaller edges first

        for u,v,w in edges:
            pu = find(u)
            pv = find(v)

            if pu==pv:
                continue

            # more weights ahead joining the components will make greater value so omit it and return first weight when we reached atmost k condition

            if rank[pu]<rank[pv]:
                parent[pu] = pv
            elif rank[pu]>rank[pv]:
                parent[pv] = parent[pu]
            else:
                parent[pv] = pu
                rank[pu] += 1
            
            components -= 1

            if components == k:
                return w