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
within the array. There are multiple solution for this, the ones I have explored are brute force and using hash table.
'''

from typing import List

class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
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
    
    def hasDuplicate2(self, nums: List[int]) -> bool: 
        # with this method we sort the list and we can confirm if there are duplicated by checking the adjacent indexes, we shift pointers if they are not duplicates
        # the sorting time takes logN, the loop time takes N, so the time complexity is O(NlogN)
        # better than brute force solution as it is faster
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    def hasDuplicate3(self, nums: List[int]) -> bool: 
        # we are going to use a hash set
        # lets us insert elements into hash set in O(1) time
        # we check if the element being added is duplicate, if not add it, if is return true
        # all operations are O(1) but had to go through the list, so running time is O(N)
        # IMPOORTANT NOTE: hash sets only store unique values, so if you have a string an it has multiple of the same letter it will only store that letter once

        hashset = set() # creating the hashset we will insert into
        for n in nums:
            if n in hashset: # check if it is in there first to check for duplicates before adding
                return True
            hashset.add(n) # add after check is false
        return False # if no duplicates found return false at the end


if __name__ == "__main__":
    print("\nSolution 1: Using brute force.")
    print("Is there a duplicate in any of these lists?")
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5]  # No duplicates
    nums2 = [3, 7, 9, 11, 22, 33, 77, 7]  # Duplicate 7
    nums1Solution = solution.hasDuplicate1(nums1)
    nums2Solution = solution.hasDuplicate1(nums2)
    print(f"Array: {nums1}\nResult: {nums1Solution}")
    print(f"Array: {nums2}\nResult: {nums2Solution}")


    print("\n")
    print("Solution 2: Using hash set")
    print("Is there a duplicate in any of these lists?")
    nums3 = [6,7,8,9,10]  # No duplicates
    nums4 = [88, 92, 33, 44, 41, 59, 44, 100, 2100]  # Duplicate 44
    nums3Solution = solution.hasDuplicate3(nums3)
    nums4Solution = solution.hasDuplicate3(nums4)
    print(f"Array: {nums3}\nResult: {nums3Solution}")
    print(f"Array: {nums4}\nResult: {nums4Solution}")
