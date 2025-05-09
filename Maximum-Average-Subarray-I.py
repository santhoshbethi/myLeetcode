class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        summ=0
        for i in range(k):
            summ+=nums[i]
        max_avg=summ/k
        for i in range(k,n):
            summ+=nums[i]
            summ-=nums[i-k]
            max_avg=max(max_avg, summ/k)
        return max_avg
        

        