class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lis_sq=[]
        for i in(nums):
            lis_sq.append(i*i)
        lis_sq.sort()
        return lis_sq