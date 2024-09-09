'''
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:

        # O(N) runtime
        # converting the number to a string
        string = str(x)
        l = 0
        r = len(string) - 1

        while l < r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    test_cases = [121, -121, 10, 12321, 98789]

    for test_value in test_cases:
        result = sol.isPalindrome(test_value)
        print(f"Is {test_value} a palindrome? {result}")
