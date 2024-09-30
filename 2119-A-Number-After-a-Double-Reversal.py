class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if 0<=num<10:
            return True
        if num % 10==0:
            return False 
        else:
            return True
        

        