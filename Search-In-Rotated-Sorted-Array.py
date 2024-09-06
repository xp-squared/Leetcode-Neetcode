'''
Binary Search Problem

Find Target in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1


'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return the index of the target
        # Example: [3,4,5,6,1,2], target = 1, the index of target is 4
        # solution runs in O(log n) time using binary search

        l = 0
        r = len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2  # getting middle of array
            if nums[mid] == target:  # if middle equals the target, we can return it
                return mid

            # We're in the left sorted portion
            if nums[l] <= nums[mid]: 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # move to the right side
                else:
                    r = mid - 1  # move to the left side
            
            # We're in the right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # move to the left side
                else:
                    l = mid + 1  # move to the right side

        return -1  # if target is not found

if __name__ == "__main__":
    solution = Solution()

    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
    print(solution.search([1], 0))  # Output: -1
    print(solution.search([1, 3], 3))  # Output: 1
