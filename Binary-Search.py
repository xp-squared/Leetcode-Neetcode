'''
Practice Counter: 2


Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums already sorted in ascending order
        # have to solve in O(log n)
        # we will have two pointers at left and right and each loop iteration we will keep finding the so-called middle

        l = 0
        r = len(nums) - 1
        while l <= r:
            middle = l + ((r - l) // 2)  # does not cause overflow like (l+r) // 2
            if nums[middle] < target:
                l = middle + 1  # because if the middle is less than target, everything before middle does not matter so we can eliminate it!
            elif nums[middle] > target:
                r = middle - 1  # if middle is greater than target we can remove everything after middle as it is not needed
            else:
                return middle
        return -1


if __name__ == "__main__":
    solution = Solution()

    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(solution.search(nums1, target1))  # Output: 4

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(solution.search(nums2, target2))  # Output: -1

    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target3 = 10
    print(solution.search(nums3, target3))  # Output: 9

    nums4 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    target4 = 4
    print(solution.search(nums4, target4))  # Output: -1

    nums5 = [1]
    target5 = 1
    print(solution.search(nums5, target5))  # Output: 0
