class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vowel_count = []
        instant_count = 0
        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    instant_count += 1
            else:
                if s[i] in vowels and s[i-k] not in vowels:
                    instant_count += 1
                elif s[i] not in vowels and s[i-k] in vowels:
                    instant_count -= 1
            vowel_count.append(instant_count)
        return max(vowel_count)
