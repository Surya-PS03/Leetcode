class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        N = len(arr)
        

        def generate():
            maxLeft = [0]*N
            maxRight = [0]*N
            maxLeft[0] = arr[0]
            maxRight[N-1] = arr[N-1]
            for i in range(1,N):
                maxLeft[i] = max(arr[i],maxLeft[i-1]+arr[i])
            

            for i in range(N-2,-1,-1):
                maxRight[i] = max(arr[i],maxRight[i+1]+arr[i])
            

            return maxLeft,maxRight
        

        left,right = generate()

        res = max(left)
        
        print(left,right)
        for i in range(1,N-1):

            res = max(res,left[i-1]+right[i+1])
        
        return res

