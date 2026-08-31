# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        criticalPoints = []

        l = 0
        p = head

        while p and l<3:
            l+=1
            p = p.next
        
        if l<3:
            return [-1,-1]
        

        prev = head
        mid = head.next
        nxt = mid.next

        i = 1
        while nxt:

            if prev.val>mid.val and nxt.val>mid.val:
                criticalPoints.append(i)
            elif prev.val<mid.val and nxt.val<mid.val:
                criticalPoints.append(i)
            
            prev = mid
            mid = nxt
            nxt = nxt.next
            i+=1
        
        if len(criticalPoints)<=1:
            return [-1,-1]

        mind = float("inf")
   
        for i in range(len(criticalPoints)-1):
            mind = min(mind,criticalPoints[i+1]-criticalPoints[i])

        maxd = criticalPoints[-1] - criticalPoints[0]
        return [mind,maxd]

        
    

