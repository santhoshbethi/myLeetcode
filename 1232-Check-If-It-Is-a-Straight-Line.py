class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<3:
            return True
        length=len(coordinates)
        i=0
        c=coordinates
        while i<length-2:
            if ((c[i+1][1]-c[i][1])*(c[i+2][0]-c[i+1][0]))!=((c[i+2][1]-c[i+1][1])*(c[i+1][0]-c[i][0])):
                return False   
            i=i+1
            

        return True
            
        