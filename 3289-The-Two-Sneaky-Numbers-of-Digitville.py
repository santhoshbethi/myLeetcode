class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        countDict={}
        for each in nums:
            if each in countDict:
                countDict[each]+=1
            else:
                countDict[each]=1
        misch_list=[]
        for key,val in countDict.items():
            if val>1:
                misch_list.append(key)
        return misch_list

        