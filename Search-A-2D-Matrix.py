'''
Binary Search Problem
Practice Counter: 2

Search 2D Matrix


You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
1  2  4  8
10 11 12 13
14 20 30 40

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: ue


Example 2:
1  2  4  8
10 11 12 13
14 20 30 40



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we will use binary search within this problem
        # we can do this search of 2D matrix in O(log r + c)
        rows = len(matrix)
        col = len(matrix[0])  # gets the length of the first row to see how many columns 
    
        # do first binary search of finding the row the target may be located in
        top = 0
        bot = rows - 1
        while top <= bot:
            middleRow = (top + bot) // 2
            if target > matrix[middleRow][-1]:  # if target is greater than the matrix in the middle row, rightmost value (which is the greatest value in that row)
                top = middleRow + 1  # moving top row down technically 
            elif target < matrix[middleRow][0]:  # if target is less than least element in middle row, we need
                bot = middleRow - 1  # moving bottom row up technically
            else:
                break  # target value may be within the current row

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l = 0
        r = col - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))  

    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))  

    matrix3 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target3 = 20
    print(solution.searchMatrix(matrix3, target3))  

    matrix4 = [[1]]
    target4 = 1
    print(solution.searchMatrix(matrix4, target4))  

    matrix5 = [[1]]
    target5 = 2
    print(solution.searchMatrix(matrix5, target5)) 
