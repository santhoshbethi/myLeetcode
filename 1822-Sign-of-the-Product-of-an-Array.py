class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product=1
        for each in nums:
            if each==0:
                return 0
            product=product*each
            
        return 1 if product >0 else -1
            


        