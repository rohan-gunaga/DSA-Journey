class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse_mapping = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in mapping and mapping[char] != word:
                return False

            if word in reverse_mapping and reverse_mapping[word] != char:
                return False

            mapping[char] = word
            reverse_mapping[word] = char
    
        return True
            

            





        
        