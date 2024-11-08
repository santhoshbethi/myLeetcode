class Solution:
    def minElement(self, nums: List[int]) -> int:
        resultList=[]
        for each in nums:
            strEach=str(each)
            sum=0
            for each in strEach:
                sum+=int(each)
            resultList.append(sum)
        return min(resultList)