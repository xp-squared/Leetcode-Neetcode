'''
Three Integer Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1: 1

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input array so we can skip the duplicates
        # for two sum remember we used hashmap and as well left and right pointers

        results = []
        nums.sort() # O(n log n) for sorting

        # (n^2) for these loops below us
        # total time complexity is O(n log n) + O(n^2): O(n^2) as it is the longer time 
        for idx, a in enumerate(nums): # for index and value a of the array
            if a > 0: # if a is greater than 0, we will never get a result that is going to equal to 0 as it would be positive numbers added together
                break
            if idx > 0 and a == nums[idx - 1]: # means if it is the same value as before, if we get -3 and then -3 is next again
                continue # continue to next iteration of this loop
            
            l = idx + 1 # so we dont accidentally cross our left pointer with a
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # if greater than 0 we need to make it smaller by moving the right pointer to the left once to a smaller number
                    r -= 1
                elif threeSum < 0: # if less we need to increase to get closer to 0 so we increase our left pointer by 1 which knowing that the list is sorted it will be a number that is bigger
                    l += 1
                else: 
                    results.append([a, nums[l], nums[r]]) # we found a case where the numbers equal 0 being added together

                    # now we need to update our pointers  
                    l += 1 # shift to the left once
                    while nums[l] == nums[l-1] and l < r: # if the new left is the same as the previous we shift left once more, we do it as long as left pointer is less than right pointer
                        l += 1
        return results


if __name__ == "__main__":
    solution = Solution()

    nums1 = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

    nums2 = []
    print(solution.threeSum(nums2))  # Output: []


    nums4 = [0, -2, 2]
    print(solution.threeSum(nums4))  # Output: [[-2, 0, 2]]

    nums5 = [-5,0,3,7,2]
    print(solution.threeSum(nums5))  # Output: [[-5, 2, 3]]
