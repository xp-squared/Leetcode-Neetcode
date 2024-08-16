'''
Daily Temperatures
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100

'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for the ith day, we want to find how many days it took for there to be a greater temperature
        # we use stack and append the day difference to the output list
        res = [0] * len(temperatures) # result array with length of temperatures and is filled with 0's, good for if a result is 0 so no case to handle that
        stack = [] # pair: [temp, index]

        for idx, temp in enumerate(temperatures): # getting the index and the value at the same time
            while stack and temp > stack[-1][0]: # temp > top of our stack and temperature of it which is the first value so 0, as well while stack is not empty
                stackT, stackInd = stack.pop() # getting the temp and the index, pop always returns the value
                res[stackInd] = idx - stackInd # getting the difference between the current day (idx) and popped day
            stack.append((temp, idx)) # append the current day
        return res


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    temperatures1 = [30, 38, 30, 36, 35, 40, 28]
    print(solution.dailyTemperatures(temperatures1))  # Output: [1, 4, 1, 2, 1, 0, 0]
    
    # Test case 2
    temperatures2 = [22, 21, 20]
    print(solution.dailyTemperatures(temperatures2))  # Output: [0, 0, 0]
    
    # Additional test cases
    temperatures3 = [30, 60, 90]
    print(solution.dailyTemperatures(temperatures3))  # Output: [1, 1, 0]
    
    temperatures4 = [30, 20, 10, 40, 50, 60]
    print(solution.dailyTemperatures(temperatures4))  # Output: [3, 2, 1, 1, 1, 0]
    
    temperatures5 = [50, 50, 50, 50]
    print(solution.dailyTemperatures(temperatures5))  # Output: [0, 0, 0, 0]
