class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j] == target:
                    return i,j
                else:
                    continue
        print("No such solution!")

class Solution2:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    target = 5
    solution = Solution2()
    end = solution.twoSum(nums,target)