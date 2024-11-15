class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return m*n
        min_x=m
        min_y=n
        for each in ops:
            min_x=min_x if each[0]>min_x else each[0]
            min_y=min_y if each[1]>min_y else each[1]
        return min_x*min_y
            



        