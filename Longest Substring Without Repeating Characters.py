class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_hashmap = {}
        max_len = -1
        left_ptr = 0
        current_len = 0
        for index, char in enumerate(s):
            if char not in letter_hashmap:
                letter_hashmap[char] = index
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                index_of_repeated_char = letter_hashmap[char]
                get_popped_str = s[left_ptr:index_of_repeated_char + 1]
                for char in get_popped_str:
                    letter_hashmap.pop(char)
                    current_len = index - index_of_repeated_char
                    left_ptr = index_of_repeated_char + 1
                letter_hashmap[char] = index
        return max_len

# create a test case
test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))