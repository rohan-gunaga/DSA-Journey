class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        for char in ransomNote:
            if ransomNote.count(char) > magazine.count(char):
                return False
            
        return True





        