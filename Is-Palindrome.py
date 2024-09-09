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
    def isPalindrome_string(self, x: int) -> bool:
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

    def isPalindrome_no_string(self, x: int) -> bool:
        # without converting to a string
        if x < 0:
            return False
        # we want to reverse the number and compare it to the original number
        reverse = 0
        temp = x  # temp will be the same number as x

        while temp != 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10
            # What is happening is we are cutting each end digit and reversing it
            # By creating x backwards, we can directly compare if it will be a palindrome

        return reverse == x


# Example of how to use the class with multiple test cases
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [121, -121, 10, 12321, 98789]

    print("Using string conversion method:")
    for test_value in test_cases:
        result = sol.isPalindrome_string(test_value)
        print(f"Is {test_value} a palindrome? {result}")

    print("\nUsing no string conversion method:")
    for test_value in test_cases:
        result = sol.isPalindrome_no_string(test_value)
        print(f"Is {test_value} a palindrome? {result}")
