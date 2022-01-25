# binary search
class Solution:
    def searchInsert(self, nums, target):

        first = 0
        last = len(nums) - 1
        while True:
            if len(nums) == 1:
                return 0 if target < nums[0] else 1
            middle = (first + last) // 2
            print(first, middle, last)

            # compare
            if nums[first] == target:
                return first
            elif nums[last] == target:
                return last
            elif nums[middle] == target:
                return middle
            elif len(nums[first:last + 1]) == 2:
                return first if target < nums[first] else last + 1 if target > nums[last] else first + 1
            else:
                if nums[middle] < target:
                    first = middle
                elif nums[middle] > target:
                    last = middle


a = Solution()
a.searchInsert([1], 0)