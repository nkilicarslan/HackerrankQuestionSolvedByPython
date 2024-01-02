class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_product = 1
        pos_product = 1
        max_product = -9999999
        for num in nums:
            if num == 0:
                neg_product = 1
                pos_product = 1
                max_product = max(max_product, 0)
            else:
                neg_tmp = neg_product
                neg_product = min(pos_product * num, neg_product * num, num)
                pos_product = max(neg_tmp * num, pos_product * num, num)
                max_product = max(max_product, pos_product)

        return max_product