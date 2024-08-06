'''
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a max heap to pop max numbers k amount of times
        # Can be solved in linear time using bucket sort algorithm
        # Bucket sort with indices being used as counts, so if you have had a single 100, it would go to i = 1 and the value 100 would be held in the values
        # Can use an array size of the input array every time and go through with it in linear time
        # Going from the top of the array to the bottom, we will eliminate each value that is empty and get our top k elements by going through it

        count = {}  # Hash map to count occurrences

        # Array of arrays that is the size of our input + 1
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # For count of the particular value, we increment its value, but if it does not already exist in count we use the get function to set the default value to 0
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():  # This will return every key-value pair in our dictionary
            # For every number and count, at count we append the value
            # This value n occurs exactly c amount of times
            freq[c].append(n)
        
        res = []
        # Starting from the end of the array, descending order
        for i in range(len(freq) - 1, 0, -1):
            # 5 to 0, decrement by -1 each time
            for n in freq[i]:
                res.append(n)  # Adding that value
                if len(res) == k:
                    return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 3, 3, 3]
    k1 = 2
    print(solution.topKFrequent(nums1, k1))  # Output: [2, 3]

    nums2 = [7, 7]
    k2 = 1
    print(solution.topKFrequent(nums2, k2))  # Output: [7]
