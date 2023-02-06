class Solution:
    def trap(self, height: List[int]) -> int:
        asw = 0
        left = [0] * len(height)
        
        for i in range(1, len(height)):
            left[i] = max(height[i-1], left[i-1])
            
        right = [0] * len(height)
        
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i+1], right[i+1])
            
        for i in range(len(height)):
            water_lvl = min(left[i], right[i])
            if water_lvl >= height[i]:
                asw += water_lvl - height[i]
                
        return asw
