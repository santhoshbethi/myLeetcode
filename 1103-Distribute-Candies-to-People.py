class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        n=1
        i=0
        while candies>0:
            if candies>n:
                res[i]+=n
            else:
                res[i]+=candies
            i=i+1
            if i+1>num_people:
                i=0
            candies=candies-n
            n+=1
        return res



