class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        key_list=list(c.keys())
        value_list=list(c.values())
        return key_list[value_list.index(max(value_list))]