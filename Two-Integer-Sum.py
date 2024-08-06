'''
Practice Counter: 
Sol 1:
Sol 2:

Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''

from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # The question is asking to return the indexes that add up to equal the target.
        # This is the brute force solution, it takes O(n^2) time because of the nested loop.
        for i in range(len(nums)):  # Start with the first number in the list.
            for j in range(i + 1, len(nums)):  # Always get the number directly after i.
                # j will iterate through the list to find a number that, when added to nums[i], equals the target.
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # hash map solution
        # were gonna have our hashmap look like this
        # this iterating through the array in one pass instead of adding all of the arrays data to the hash map from the start
        # time complexity: O(N)
        # memory: O(N), we could potentially add every value to hashmap
        
        prevMap = {} # val : index 
        # starts a loop that iterates over the list nums with both the 
        # index (i) and the number (n). The enumerate function is used to 
        # keep track of both the index and the value.
        for index, currentNumber in enumerate(nums):
            # calcs difference between target and current value n
            diff = target - currentNumber

            # if that difference is in the map already we know that we have found the values that make the target
            if diff in prevMap:
                return[prevMap[diff],index]
                
            # if not though we add the current number and its index to the hashmap
            prevMap[currentNumber] = index # {3 : 0}
        return

        ''' 
        nums = [3, 4, 5, 6] and target = 7.
        First Iteration (index=0, currentNumber=3):
        diff = 7 - 3 = 4
        prevMap is {}, so diff (which is 4) is not found.
        Update prevMap to {3: 0}.
        
        Second Iteration (index=1, currentNumber=4):
        diff = 7 - 4 = 3
        prevMap is {3: 0}, and diff (which is 3) is found.
        Return [prevMap[3], 1], which is [0, 1].
        return[prevMap[diff],index] so we get the index of where 3 was and get our current index to return
        '''



if __name__ == "__main__":
    print()
    solution = Solution()
    nums1 = [3, 4, 5, 6]
    target1 = 7
    print(solution.twoSum1(nums1, target1))  # Output: [0, 1]

    nums2 = [4, 5, 6]
    target2 = 10
    print(solution.twoSum1(nums2, target2))  # Output: [0, 2]

    nums3 = [5, 5]
    target3 = 10
    print(solution.twoSum1(nums3, target3))  # Output: [0, 1]

    nums4 = [4, 5]
    target4 = 11
    print(solution.twoSum1(nums4, target4))  # Output: None

    print()
    print()

    print(solution.twoSum2(nums1, target1))  # Output: [0, 1]
    print(solution.twoSum2(nums2, target2))  # Output: [0, 2]
    print(solution.twoSum2(nums3, target3))  # Output: [0, 1]
    print(solution.twoSum2(nums4, target4))  # Output: None
    print()



