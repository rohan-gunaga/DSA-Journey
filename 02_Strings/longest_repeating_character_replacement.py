class Solution(object):
    def characterReplacement(self, s, k):
        k = 0
        max_freq = 0
        current_freq = 0
        left = 0
        window_length = 0
        right = 0 

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

            max_freq = max(freq.values())
            
            while window_length - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            freq[s[right]] = freq.get(s[right], 0) + 1





        
        




    
     
    