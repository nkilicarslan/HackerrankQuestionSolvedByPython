class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr <= right_ptr:

            if nums[left_ptr] < nums[right_ptr]:
                return min(res, nums[left_ptr])

            middle = (left_ptr + right_ptr) // 2
            res = min(res, nums[middle])

            if nums[left_ptr] < nums[middle]:
                left_ptr = middle + 1
            else:
                right_ptr = middle - 1

        return res
