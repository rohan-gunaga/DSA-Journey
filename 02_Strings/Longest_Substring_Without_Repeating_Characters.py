class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
       seen = set()
       left = 0
       max_length = 0

       for right, char in enumerate(s):

            while char in seen:
                seen.remove(s[left])
                left += 1

            
            seen.add(char)

            current_length = right - left + 1
            max_length = max(max_length, current_length)

       return max_length



       

                





        
        

            
                
