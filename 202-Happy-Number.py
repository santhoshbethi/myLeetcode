class Solution:
    def isHappy(self, n: int) -> bool:
 
        
        seenList=[]
        
        while n>0:
            if n==1:
                return True
            else:
                
                
                if n in seenList:
                    return False
                else:
                    seenList.append(n)
                    n=self.calculateSum(n)
                    

    def calculateSum(self,n):
        sum=0
        while n>0:
            num=n%10
            sum=sum+(num*num)
            n=n//10
        return sum

