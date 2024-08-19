'''
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
'''

from typing import List

class Solution:
    # Given an array of integers numbers that is sorted in non-decreasing order!!!!
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0  # left most element of list index
        r = len(numbers) - 1  # right most element of list index
        while l < r:
            # our numbers array is sorted in non decreasing order, no element is less than the previous one
            # we grab our current sum from the starting indexes
            currentSum = numbers[l] + numbers[r]
            if currentSum < target:  # if our currentSum is less than the target, we know we can increase our left pointer since it is non decreasing and we will have a bigger sum after
                l += 1
            elif currentSum > target:  # if our currentSum is greater than the target we can decrease our right pointer leading to a smaller number to use to possibly find the target
                r -= 1
            else:
                return [l + 1, r + 1]  # based on 1 so add 1 to each of them, returns the index


if __name__ == "__main__":
    solution = Solution()
    
    numbers1 = [1, 2, 3, 4]
    target1 = 3
    print(solution.twoSum(numbers1, target1))  # Output: [1, 2]

    numbers2 = [2, 7, 11, 15]
    target2 = 9
    print(solution.twoSum(numbers2, target2))  # Output: [1, 2]

    numbers3 = [5, 25, 75]
    target3= 100
    print(solution.twoSum(numbers3, target3))  # Output: [2, 3]

    numbers4 = [10, 20, 30, 40, 50]
    target4 = 70
    print(solution.twoSum(numbers4, target4))  # Output: [2, 5]
