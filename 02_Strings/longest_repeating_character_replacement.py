class Solution(object):
    def characterReplacement(self, s, k):
        
        max_length = 0
        left = 0
        freq = {}
        window_length = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(freq.values())

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            window_length = right - left + 1
            max_length = max(max_length, window_length)

        return max_length






        
        


        
        




    
     
    