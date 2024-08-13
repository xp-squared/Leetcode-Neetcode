'''
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7
'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # given a certain number of pair of parentheses and have to generate different combinations of them that are nested validly
        # like (()) or (()()) or ()()(), 
        # n = 3, 3 pairs, 3 open 3 close
        # as parentheses are being added add to the open and close counter until it matches 
        # can start with open parentheses but never closed parentheses
        # can only add closing parentheses if close < open count
        # the tree made at the 6 minute mark explains well of how many different options there may be
        
        # only add open parentheses if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n
        # doing the problem recursively
        stack = []
        result = []
        # dont have to pass the list/stack or n into function below since it is nested
        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack)) # joining every character in the stack together and appending it to the result
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        # outside of function
        backtrack(0,0) # calling 0 for initial open and close count
        return result

        # Explaining if n = 2
        # openN = 0 < 2 so we append (
        # openN = 1 < 2 so we append (
        # openN = 2 < 2 we skip that part
        # closedN = 0 < openN = 2, append )
        # closedN = 1 < openN = 2, append )
        # openN == closedN == n so we append that result
        # that result is (())
        # now return
        # pop ), nothing after to do return to previous level
        # pop ), nothing after to do return to previous level
        # pop (, now move onto the if statement after it
        # the only thing currently in our stack is ( as we our still in our second level of recursion
        # append ) cos closedN is less than openN, now both are 1 as we go into the next level
        # append (
        # now we are going into next level (2,1,2)
        # append ), now we are at (2,2,2)
        # return ()()
        # pop )
        # pop (
        # closedN and openN = 1
        # pop )
        # return to level 1 and pop (
        # return final results


if __name__ == "__main__":
    solution = Solution()
    result = solution.generateParenthesis(2)
    print(result)  # Output should be ["(())", "()()"]
