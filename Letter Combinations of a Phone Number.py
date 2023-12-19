class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_mapping_to_char = {}
        num_mapping_to_char['2'] = ['a', 'b', 'c']
        num_mapping_to_char['3'] = ['d', 'e', 'f']
        num_mapping_to_char['4'] = ['g', 'h', 'i']
        num_mapping_to_char['5'] = ['j', 'k', 'l']
        num_mapping_to_char['6'] = ['m', 'n', 'o']
        num_mapping_to_char['7'] = ['p', 'q', 'r', 's']
        num_mapping_to_char['8'] = ['t', 'u', 'v']
        num_mapping_to_char['9'] = ['w', 'x', 'y', 'z']

        res = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return num_mapping_to_char[digits[0]]

        res = num_mapping_to_char[digits[0]]
        for i in range(1,len(digits)):
            tmp_list = []
            for comb in res:
                for val in num_mapping_to_char[digits[i]]:
                    tmp_list.append(comb + val)
            res = tmp_list[:]

        return res
