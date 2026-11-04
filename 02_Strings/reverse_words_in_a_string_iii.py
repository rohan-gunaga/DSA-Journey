class Solution(object):
    def reverseWords(self, s):

        words = s.split()

        reversed_words = []
        
        for word in words:
            reversed_words.append(word[::-1])

        return " ".join(reversed_words)



        


        
            


        
        