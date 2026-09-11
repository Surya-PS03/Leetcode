# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None

        heap = [(list1.val,1,list1),(list2.val,2,list2)]
        heapq.heapify(heap)

        newHead = ListNode(0)
        p = newHead
        while heap:
        
            _,idx,temp = heapq.heappop(heap)

            p.next = temp

            p = temp

            if temp.next != None:
                heapq.heappush(heap,(temp.next.val,idx,temp.next))
        
        p.next = None
        
        return newHead.next
            