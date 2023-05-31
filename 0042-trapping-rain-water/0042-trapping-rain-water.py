class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        highest = max(height)

        # 왼쪽부터 구하기
        top = 0
        for i in range(height.index(highest)):
            if height[i] >= top:
                top = height[i]
            else:
                water += (top - height[i])

        # 오른쪽 구하기
        top = 0
        for i in range(len(height) - 1, height.index(highest), -1):
            if height[i] >= top:
                top = height[i]
            else:
                water += (top - height[i])

        return water
            
        
            

        