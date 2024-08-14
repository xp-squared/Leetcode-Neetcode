'''
Practice Counter:
Sol1: 1


Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.



Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
'''

class Solution:
    # everything has running time of O(1)
    def isValid(self, s: str) -> bool:
        # This is a stack problem, we are returning a boolean.
        # Stack is LIFO (Last In, First Out).
        stack = []
        # Hash map for deciding the parenthesis match.
        closeToOpen = {")": "(", "]": "[", "}": "{"}  # Every key is a closing bracket.
        # Closing brackets need to match the opening brackets.
        # The idea is to use the hash map to match the parenthesis on the stack and pop them out if they do match.
        # Time complexity O(N) (and memory) because we just go through the list once.

        for c in s:  # Going through every character in the string.
            if c in closeToOpen:  # Checking if closing parenthesis.
                # Cannot add closing parenthesis to empty stack and make sure the value at the top of the stack matches the opening parenthesis, that's why we use "stack" in our if statement.
                # stack[-1] is the value at the top of the stack, last value added.
                # Remember c in this loop is always going to be the closing bracket.
                if stack and stack[-1] == closeToOpen[c]:  # Meaning that they match each other.
                    # print(stack[-1], "==", closeToOpen[c], " popped")
                    stack.pop()
                else:
                    return False
            else:  # Getting an open parenthesis, we can add as many as we want.
                # print(c, " was appended")
                stack.append(c)
        # Can only return true if the stack is empty, otherwise it is false because we did not pop everything meaning there was mismatched parenthesis.
        return True if not stack else False
    
    # example run with the first input: s1 = "()[]{}"
    # first we append ( to the stack is that is an opening parentheses
    # next we go to ), we go through with our if statement as it is in closeToOpen
    # we check if it matches whats on top of the stack by checking top with stack[-1] which is ( that we appended
    # we do == to closeToOpen[c] which takes our current character ) and matches it to its opening in the map which ( which confirms that they are together
    # this process repeats


if __name__ == "__main__":
    solution = Solution()
    s1 = "()[]{}"
    print(solution.isValid(s1))  # Output: True
    print()

    s2 = "(]"
    print(solution.isValid(s2))  # Output: False

    s3 = "([)]"
    print(solution.isValid(s3))  # Output: False

    s4 = "{[]}"
    print(solution.isValid(s4))  # Output: True
