class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_profit = float("-inf")
        current_value = float("-inf")
        for number in nums:
            if (current_value < 0 and number >= 0) or (current_value < 0 and number < 0):
                current_value = number
            elif (current_value > 0 and number > 0) or (current_value > 0 and number < 0):
                current_value += number
            max_profit = max(max_profit, current_value)
        return max_profit