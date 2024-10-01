class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign=1
        sum=0
        for each in str(n):
            sum=sum+(int(each)*sign)
            
            sign= -1 if sign==1 else 1
        return sum


        