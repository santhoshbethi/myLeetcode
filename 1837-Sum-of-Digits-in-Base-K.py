class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n==0:
            return 0
        res=0
        while n:
            res+=n%k
            n=n//k
        return res

