class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1=0
        sum2=0
        for num in nums:
            if num<10:
                sum1+=num
            else:
                sum2+= num
        return True if sum1!=sum2 else False
       


        