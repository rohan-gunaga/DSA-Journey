class Solution(object):
    def isAnagram(self, s, t):

        
        if len(s) != len(t):
            return False

        count_s = {}
    
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

            if count_s == count_t:
                return True
            else:
                return False

        



        