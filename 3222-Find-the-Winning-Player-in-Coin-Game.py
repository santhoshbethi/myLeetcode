class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if x<1 or y<4:
            return "Bob"
        count=0
        while x or y:
            
            count+=1
            x-=1
            y-=4
            if x==0 or y<4:
            
                return "Alice" if count%2!=0 else "Bob"


        