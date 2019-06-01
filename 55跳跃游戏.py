class Solution:
    def canJump(self, nums) -> bool:
        if not nums or len(nums) == 1:
            return True
        flag = []
        n = len(nums)
        def oneJump(now_index):
            if nums[now_index] + now_index >= n - 1:
                flag.append(1)
                return
            else:
                for i in range(nums[now_index], 0, -1):
                    oneJump(now_index + i)

        oneJump(0)
        return bool(flag)

class Solution:
    def canJump(self, nums) -> bool:
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < n - 1:
            end = max(end, nums[start] + start)
            start += 1
        return end >= n - 1

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        i = n - 2
        end = n - 1
        while i >= 0:
            if nums[i] + i >= end:
                end = i
            i -= 1

        return end >= 0




s = Solution()
print(s.canJump([3,2,1,0,4]))