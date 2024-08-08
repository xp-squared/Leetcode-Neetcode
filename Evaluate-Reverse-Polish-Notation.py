'''
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Reverse Polish Notation = POSTFIX NOTATION 
        # This is a stack problem
        # Has time complexity of O(N), traversing the list once
        stack = []
        for c in tokens:
            # If c is an operator, we need to take the previous operators and perform the operation
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # Want to round towards zero and convert the answer to an integer
                stack.append(int(b / a))
            else: 
                # If it is not an operator, we convert the string to an int and append to our stack
                stack.append(int(c))
        # Returning the final value after all operations have been performed
        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    tokens1 = ["2", "1", "+", "3", "*"]
    print(solution.evalRPN(tokens1))  # Output: 9

    tokens2 = ["4", "13", "5", "/", "+"]
    print(solution.evalRPN(tokens2))  # Output: 6

    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(solution.evalRPN(tokens3))  # Output: 22
