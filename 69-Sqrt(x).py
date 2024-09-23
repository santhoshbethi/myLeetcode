class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l=0
        h=x
        ans=0
        while l<=h:
            m=(l+h)//2
            if m**2 >x:
                h=m-1

            elif m**2<x:
                l=m+1
                ans=m
            else:
                print("here",m)
                return m
        return ans
        