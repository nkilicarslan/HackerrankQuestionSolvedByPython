class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        all_nums = {}
        for number in nums:
            if number not in all_nums:
                all_nums[number] = 1
            else:
                return True
        return False