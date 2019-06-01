class Solution:
    def trap(self, height):
        if not height or len(height) < 3:
            return 0
        ans = 0
        for i in range(1, len(height) - 1):
            max_l = max_r = 0
            for l in range(i):
                if height[l] >= max_l and height[l] > height[i]:
                    max_l = height[l]
            for r in range(i+1,len(height)):
                if height[r] >= max_r and height[r] > height[i]:
                    max_r = height[r]
            if max_l > 0 and max_r > 0:
                ans += min(max_l, max_r) - height[i]
        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))