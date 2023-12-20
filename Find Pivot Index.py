class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        sum_up_to = 0
        for i in range(len(nums)):
            if sum_up_to == (total_sum - sum_up_to - nums[i]):
                return i
            sum_up_to += nums[i]
        return -1