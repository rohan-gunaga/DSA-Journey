class Solution(object):
    def maxVowels(self, s, k):

        vowel_count = 0

        for i in range(k):
            if s[i] in "aeiou":
                vowel_count += 1

        max_vowels = vowel_count

        for i in range(k, len(s)):
            vowel_count -= s[i-k] in "aeiou"
            vowel_count += s[i] in "aeiou"

            max_vowels = max(max_vowels, vowel_count)

        return max_vowels