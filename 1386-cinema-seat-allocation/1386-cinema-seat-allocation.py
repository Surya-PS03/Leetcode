from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        occupied = defaultdict(int)

        for row,seat in reservedSeats:
            occupied[row] = occupied[row] | (1<<seat)

        # block masks

        # block1
        block1 = (1<<2) | (1<<3) | (1<<4) | (1<<5)
        # block2
        block2 = (1<<4) | (1<<5) | (1<<6) | (1<<7)
        # block3
        block3 = (1<<6) | (1<<7) | (1<<8) | (1<<9)

        count = (n-len(occupied))*2


        for row,mask in occupied.items():

            if mask&block1==0:
                mask = mask | block1
                count += 1
            
            if mask&block2==0:
                mask = mask | block2
                count += 1

            if mask&block3==0:
                mask = mask | block3
                count += 1
            

        return count