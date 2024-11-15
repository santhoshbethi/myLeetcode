class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return \0\
        res=\\
        sign=-1 if num<0 else 1
        num=abs(num)
        while num>0:
            rem=num%7
            num=num//7
            res+=str(rem)
        if sign<0:
            res=res+'-'
        return res[::-1]

        