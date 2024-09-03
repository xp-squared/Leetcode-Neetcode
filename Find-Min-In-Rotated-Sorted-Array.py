'''
Find Minimum in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search problem but not traditional whatsoever
        # example
        # you have array nums = [1,2,3,4,5]
        # it would be [3,4,5,1,2] if it was rotated 4 times.
        # return minimum element of this array in O(log N) time

        start = 0
        end = len(nums) - 1
        curr_min = float("inf") # make the current minimum the largest number possible so we can have our start minimum be as large as it is

        while start < end:
            middle = start + (end - start ) // 2 # accounts for going out of bounds with indexes
            curr_min = min(curr_min, nums[middle]) # grab the current minimum
            # if middle value is in left sorted portion of values and is greater we know we want to go to the right sorted portion of values as they will be smaller

            # right has the min
            # [3, 4, 5, 1, 2]
            # mid (5) is > end (2)
            # update start to mid + 1 as we know it will not be on the left side any more
            if nums[middle] > nums[end]: # the middle of the list is more than the end of the list 
                start = middle + 1
            
            # left has the min
            # [3, 4, 1, 2]
            # this would be the case that 1 is the middle, which would be our current min
            # we would search to the left
            # in this case though we already found our minimum
            else:
                end = middle - 1

        return min(curr_min, nums[start])


if __name__ == "__main__":
    solution = Solution()

    print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
    print(solution.findMin([11, 13, 15, 17]))  # Output: 11
    print(solution.findMin([2, 1]))  # Output: 1
    print(solution.findMin([1]))  # Output: 1
