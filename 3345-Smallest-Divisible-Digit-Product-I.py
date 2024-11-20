class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        product=1
        act_number=n
        while n:
            product=product*(n%10)
            n=n//10

        if product%t!=0:

            return self.smallestNumber(act_number+1,t)
        # else:
        #     return act_number
        return act_number
 
 
        