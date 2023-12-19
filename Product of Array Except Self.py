class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            if nums.count(0) == 1:
                index_of_zero = nums.index(0)
                count = 1
                for num in nums:
                    if num == 0:
                        continue
                    else:
                        count *= num
                res = [0] * len(nums)
                res[index_of_zero] = count
                return res
            else:
                return [0] * len(nums)
        total_product = 1
        for num in nums:
            total_product *= num
        res = [total_product//num for num in nums]
        return res