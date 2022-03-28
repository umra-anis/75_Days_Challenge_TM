class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i, digit in enumerate(nums):
            if left_sum == (total-left_sum-digit) :
                return i
            left_sum+=digit
        return -1