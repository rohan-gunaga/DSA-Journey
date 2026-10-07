class Solution(object):
    def checkInclusion(self, s1, s2):

        s1_count = {}
        window_count = {}

        for char in s1:
            if char in s1_count:
                s1_count[char] += 1
            else:
                s1_count[char] = 1

        window = s2[0:len(s1)]
        
        for char in window:
            if char in window_count:
                window_count[char] += 1
            else:
                window_count[char] = 1

        if window_count == s1_count:
            return True
        else:
            return False



        



        





        




        

        


        
        