class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_num = max(candies)
        res = []
        for candie_val in candies:
            if candie_val + extraCandies >= max_num:
                res.append(True)
            else:
                res.append(False)

        return res