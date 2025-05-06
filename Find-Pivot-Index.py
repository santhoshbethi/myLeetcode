class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        rigthSum=0
        n=len(nums)
        prefixSumArr=[0]*n
        prefixSumArr[0]=nums[0]
        for i in range(1,n):
            prefixSumArr[i]=prefixSumArr[i-1]+nums[i]
        
        # [1, 8, 11, 17, 22, 28]
            

        for i in range(n):
            
            
            if i==0:
                leftSum=0
            else:
                leftSum=prefixSumArr[i-1]
            if i==n-1:
                rightSum=0
            else:
                rightSum=prefixSumArr[n-1]-prefixSumArr[i]
            if leftSum==rightSum:
                return i
        return -1