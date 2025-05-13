class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]

        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return
            #dont pick elements:
            backtrack(i+1)

            #pick element.
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res


        