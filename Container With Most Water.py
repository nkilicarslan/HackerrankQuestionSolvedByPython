class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_val = 0
        while left_ptr < right_ptr:
            min_val = min(height[left_ptr], height[right_ptr])
            calc_val = min_val * (right_ptr - left_ptr)
            max_val = max(max_val, calc_val)
            if min_val == height[left_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_val