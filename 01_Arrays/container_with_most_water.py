class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        best_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            if current_area > best_area:
                best_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best_area 
        

        