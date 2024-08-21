'''
Practice Counter: 

Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashing / array problem
        # solution must run O(n) time complexity
        # if we just sorted it that would make our runtime n log n
        # we want to find the longest consecutive number chain in the list
        # so if the list was [1, 9, 7, 2, 8, 11, 10] our longest consec numbers would be 7, 8, 9, 10, 11 as they follow after each other 5 times

        # creating a hash set of all the numbers, removing all duplicates 
        numSet = set(nums)  
        longest = 0

        # can get start of each sequence by just looking array of numbers and see what doesn't have a left neighbor
        # when traversing through a numset remember we go through with numerical order, start from lowest number

        for n in numSet:
            if (n - 1) not in numSet: # this is how we check if it has a left neighbor or not deciding if we should check if there is a sequence
                length = 1 # knowing that we can start giving it a length as it might be a sequence
                while (n + length) in numSet: # "while 2 + 1 (3) in numSet" we add to the length if that consecutive number is in here and continuously do so until the loop breaks
                    length += 1
                longest = max(length, longest) # determine if that is the longest sequence currently or if we already found a longer one
        return longest

        # runtime and memory are both O(n)
        

if __name__ == "__main__":
    
    solution = Solution()
    
    nums1 = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums1))  # Output: 4

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(solution.longestConsecutive(nums2))  # Output: 9

    nums3 = []
    print(solution.longestConsecutive(nums3))  # Output: 0

    nums4 = [1, 2, 0, 1]
    print(solution.longestConsecutive(nums4))  # Output: 3

    nums5 = [9, 1, -3, 2, 4, 8, 3, 0, -1, -2]
    print(solution.longestConsecutive(nums5))  # Output: 8
