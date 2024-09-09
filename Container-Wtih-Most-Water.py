'''
Practice counter: 2

Two pointer problem

Max Water Container
You are given an integer array heights where heights[i] represents the height of the i^th  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

'''

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # given list of heights, wanna calculate areas between two bars to get the max area where water can be stored
        # we can solve this using brute force and multiple loops going through the list, that time complexity would be O(n^2)
        l = 0
        r = len(heights) - 1
        result = 0

        # this is o(N) time complexity
        while l < r:
            # we get our max result of area from this, we compare our result with the minimum of heights, as if we chose the larger height water would spill, times the width of the section
            # think of this line below as width * height, width of the distance from each other, times the minimum height so water does not spill
            area = (r - l ) * min(heights[l],heights[r])
            res = max(res, area)

            # if height at left is less than height at right, we increment our left pointer and want to maximize the height
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return result


if __name__ == "__main__":
    solution = Solution()

    
    heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(heights1))  # Output: 49

    heights2 = [1, 1]
    print(solution.maxArea(heights2))  # Output: 1

    heights3 = [4, 3, 2, 1, 4]
    print(solution.maxArea(heights3))  # Output: 16

    heights4 = [1, 2, 1]
    print(solution.maxArea(heights4))  # Output: 2

    heights5 = [1, 2, 4, 3]
    print(solution.maxArea(heights5))  # Output: 4