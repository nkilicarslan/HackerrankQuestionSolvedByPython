class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        s_pointer = 0
        for i in range(len(t)):
            if s_pointer == len(s):
                return True
            if s[s_pointer] == t[i]:
                s_pointer += 1

        if s_pointer == len(s):
            return True
        else:
            return False