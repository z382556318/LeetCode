class Solution:
    def partition(self, num, left, right):
        key = num[left]
        while left < right:
            while num[right] >= key and right > left:
                right -= 1
            num[left] = num[right]
            while num[left] <= key and right > left:
                left += 1
            num[right] = num[left]
        num[left] = key

        return left

    def quickSort(self, num, left, right):
        if left < right:
            q = self.partition(num, left, right)

            self.quickSort(num, left, q)
            self.quickSort(num, q+1, right)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if not nums1 and not nums2: return

        new = nums1 + nums2
        l = len(new)
        self.quickSort(new, 0, l-1)

        if l % 2 == 1:
            return new[l//2]
        else:
            return (new[l//2] + new[l//2 - 1]) / 2


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if not nums1 and not nums2: return
        if not nums2 or not nums1:
            nums = nums2 if not nums1 else nums1
            if len(nums) % 2 == 0:
                return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
            else:
                return nums[len(nums)//2]

        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m




if __name__ == '__main__':
    a = [1,2]
    b = [3,4]
    c = [1,2,6,3,4,3]
    print(Solution().findMedianSortedArrays(a, b))