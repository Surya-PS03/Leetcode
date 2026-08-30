class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        N = len(nums)

        if N==1:
            return 1
        elif N==2:
            return 2

        # left iterate

        both = 2
        leftCount = 0
        maxElm = max(nums)
        minElm = min(nums)

        for i in range(N):
            if both==0:
                break
            if nums[i]==maxElm or nums[i]==minElm:
                both-=1
            leftCount+=1
        

        # rigth iteration

        both = 2
        rightCount = 0

        for i in range(N-1,-1,-1):
            if both == 0:
                break
            if nums[i]==maxElm or nums[i]==minElm:
                both-=1
            rightCount+=1

        # if deleted from left now delete from right
        leftRightCount = 0
        for i in range(N):

            if nums[i]==maxElm or nums[i]==minElm:
                flag = 1
                leftRightCount+=1

                for j in range(N-1,i,-1):
                    if nums[j]==maxElm or nums[j]==minElm:
                        leftRightCount+=1
                        flag = 0
                        break
                    leftRightCount+=1
                    
                if flag==0:
                    break
            leftRightCount+=1

        
        rightLeftCount = 0

        for i in range(N-1,-1,-1):
            if nums[i]==maxElm or nums[i]==minElm:
                flag = 1
                rightLeftCount+=1

                for j in range(0,i):

                    if nums[j]==maxElm or nums[j]==minElm:
                        rightLeftCount+=1
                        flag=0
                        break
                    rightLeftCount+=1
                
                if flag==0:
                    break
            rightLeftCount+=1

        print(leftCount,rightCount,leftRightCount,rightLeftCount)
        return min(leftCount,rightCount,leftRightCount,rightLeftCount)