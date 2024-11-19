class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_operations=0
        for each in nums:
            num_operations+=min(each%3,3-(each%3))
        return num_operations