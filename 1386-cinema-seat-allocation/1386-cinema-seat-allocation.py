from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        occupied = defaultdict(set)

        for row,seat in reservedSeats:
            occupied[row].add(seat)

        row_occ = len(occupied)

        block1 = set((2,3,4,5))
        block2 = set((4,5,6,7))
        block3 = set((6,7,8,9))
        
        count = (n-row_occ)*2
        for row in occupied.keys():
            occ = occupied[row]
            if len(block1-occ)==len(block1):
                occ = occ | block1
                count+=1
            
            if len(block2-occ)==len(block2):
                occ = occ|block2
                count+=1
            
            if len(block3-occ)==len(block3):
                occ =  occ | block3
                count+=1

        return count

