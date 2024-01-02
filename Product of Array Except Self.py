class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_arr = []
        left_pre = 1
        right_pre = 1
        for number in nums:
            res_arr.append(left_pre)
            left_pre *= number
        for index in range(len(nums)):
            res_arr[len(nums) - index - 1] *= right_pre
            right_pre *= nums[len(nums) - index - 1]
        return res_arr
