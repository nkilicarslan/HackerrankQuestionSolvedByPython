class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = ""
        res = []
        for digit in digits:
            number += str(digit)

        number = str(int(number) + 1)
        for num in number:
            res.append(int(num))
        return res