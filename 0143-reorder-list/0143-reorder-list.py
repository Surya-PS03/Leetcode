# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        nodes = []
        p = head

        while p:
            nodes.append(p)
            p = p.next
        

        i = 0
        j = len(nodes) - 1

        while i<j:
            
            # update next of current node i to node at jth index
            nodes[i].next = nodes[j]
            i+=1

            # after connecting if they come at same index break
            if i==j:
                break

            # since i was shifted to next node after updating next of node[i] if i and j are not at same index, so update next of node[j]
            nodes[j].next = nodes[i]

            j-=1
        

        nodes[i].next = None
    