class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        tens = 0


        for deno in bills:

            if deno==5: five+=1

            elif deno==10:
                if five: 
                    five-=1
                    tens+=1
                else: return False
            
            else:
                if five and tens:
                    five-=1
                    tens-=1

                elif five>=3: five-=3
                else: return False
        
        return True