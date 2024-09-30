class Solution:
    def check_prime(self,num:int):
        
        if num<2:
            return False
        for each in range(2,int(sqrt(num)) + 1):
            if num%each==0:
                return False
        return True


    def nonSpecialCount(self, l: int, r: int) -> int:
        prime=0
        total_nums=r-l+1
        sqrtofl=math.ceil(sqrt(l))
        sqrtofr=int(sqrt(r))
        for each in range(sqrtofl,sqrtofr+1):
            if self.check_prime(each):
                prime+=1
        return total_nums-prime
                
    
            
