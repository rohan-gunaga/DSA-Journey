class Solution(object):
    def checkInclusion(self, s1, s2):

        
        s1_count = {}
        window_count = {}
        left = 0
        right = len(s1)

        if len(s1) > len(s2):
            return False

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
        
        while right < len(s2):
            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            if s2[right] in window_count:
                window_count[s2[right]] += 1
            else:
                window_count[s2[right]] = 1

            if window_count == s1_count:
                return True

            left += 1
            right += 1    
        
        return False


        



        





        




        

        


        
        
        
        


        



        





        




        

        


        
        