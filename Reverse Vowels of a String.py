class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels_list = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        # create two pointer which one of them pointing the
        # start of the array, and the other one is pointing the
        # end of the array

        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            if s[left_ptr] in vovels_list:
                if s[right_ptr] in vovels_list:
                    tmp = s[left_ptr]
                    s[left_ptr] = s[right_ptr]
                    s[right_ptr] = tmp
                    left_ptr += 1
                right_ptr -= 1
            else:
                if s[right_ptr] not in vovels_list:
                    right_ptr -= 1
                left_ptr += 1
        return ''.join(s)