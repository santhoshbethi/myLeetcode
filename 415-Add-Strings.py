class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num2=num2[::-1]
        num1=num1[::-1]
        res_length=len(num2) if len(num2)>len(num1) else len(num1)
        if len(num1)<res_length:
            append_len=res_length-len(num1)
            for _ in range(append_len):
                num1=num1+\0\
        if len(num2)<res_length:
            append_len=res_length-len(num2)
            for _ in range(append_len):
                num2=num2+\0\
        res=[]
        i=0
        carry=0
        while res_length>i:
            temp=int(num1[i])+int(num2[i])+carry

            carry=temp//10
            temp=temp%10
            print(temp)
            res.append(str(temp))
            i+=1
        
        if carry:
            res.append(str(carry))
        return  \\.join(res[::-1])
                
            

        
             

        