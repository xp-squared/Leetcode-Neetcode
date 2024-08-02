'''
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false


In my own words: we have to explore each integer array and compare the values to see if there is a value that appears more than once
within the array. There are multiple solution for this, the ones I have explored are brute force and using hash table
'''

from typing import List

class BruteForceSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force solution with O(n^2) time complexity
        # We use one nested loop and one outer loop
        # The outer loop keeps hold of one number while the inner loop goes through the list comparing to that current number
        for i in range(len(nums)):
            current = nums[i]
            # We start from i + 1 each time so we do not compare our current element with itself
            for j in range(i + 1, len(nums)):
                if current == nums[j]:
                    return True
        return False


if __name__ == "__main__":
    print("\nSolution 1: Using brute force.")
    print("Is there a duplicate in any of these lists?\n")
    solution = BruteForceSolution()
    nums1 = [1, 2, 3, 4, 5]  # No duplicates
    nums2 = [3, 7, 9, 11, 22, 33, 77, 7]  # Duplicate 7

    nums1Solution = solution.hasDuplicate(nums1)
    nums2Solution = solution.hasDuplicate(nums2)


    print(f"Array: {nums1}\nResult: {nums1Solution}")
    print()
    print(f"Array: {nums2}\nResult: {nums2Solution}")
