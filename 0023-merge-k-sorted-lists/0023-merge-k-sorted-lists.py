# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapq.heapify(heap)
        for i,l in enumerate(lists):

            if l :
                heapq.heappush(heap,(l.val,i,l))
            

        head = ListNode(0)
        p = head

        while heap:
           
            x, idx ,node = heapq.heappop(heap)

            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next))
        
        return head.next