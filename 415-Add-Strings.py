class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num2=num2[::-1]
        num1=num1[::-1]
        res_length = max(len(num1), len(num2))
        num1 = num1.ljust(res_length, '0')
        num2 = num2.ljust(res_length, '0')
        res=[]
        i=0
        temp=0
        carry=0
        while res_length>i:
            temp=int(num1[i])+int(num2[i])+carry

            carry=temp//10
            temp=temp%10
            res.append(str(temp))
            i+=1
        if carry:
            res.append(str(carry))
        return \\.join(res[::-1])
                
            

        
             

        