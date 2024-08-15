'''
Practice Counter:
Sol2: 1

Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        # two pointers section
        # part of blind 75 questions
        # we are ignoring upper and lower case
        # first solution, convert all to lowercase and remove special characters
        newStr = ""
        for c in s:
            if c.isalnum(): # if c is a-z and 0-9 we will go thru with it
                newStr += c.lower()
        return newStr == newStr[::-1] # syntax for reversing string
    
        # interviewer probably wont want us to use the functions so much to solve
        # as well we used extra memory by making newStr
        # good solution but not best for interviews

    def isPalindrome2(self, s: str) -> bool:
        # this is using 2 pointers, a left and a right pointer
        # they move their respective directions until they either meet each other or pass each other
        # to make our own alphanumeric function we are going to use ASCII values to make sure we only use letters and numbers
        # memory complexity O(1), not using any extra memory

        l = 0
        r = len(s) - 1

        while l < r:  # the pointers have not crossed each other 
            while l < r and not self.alphaNum(s[l]):  # incrementing if not in our alphaNum function
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():  # comparing characters of left and right and converting them to lowercase
                return False
            # after doing comparison want to update our left and right pointers
            l = l + 1
            r = r - 1

        return True

    def alphaNum(self, c):
        # can get ASCII val by using ord function
        # will only return something within the bounds given
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z')  or 
                ord('0') <= ord(c) <= ord('9'))



if __name__ == "__main__":
    solution = Solution()
    
    
    test_str1 = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome1(test_str1))  # Output: True
    
    test_str2 = "race a car"
    print(solution.isPalindrome1(test_str2))  # Output: False

    test_str3 = " "
    print(solution.isPalindrome1(test_str3))  # Output: True

    
    test_str4 = "Was it a car or a cat I saw?"
    print(solution.isPalindrome2(test_str4))  # Output: True

    test_str5 = "tab a cat"
    print(solution.isPalindrome2(test_str5))  # Output: False

    test_str6 = "No 'x' in Nixon"
    print(solution.isPalindrome2(test_str6))  # Output: True

    test_str7 = "Able was I, I saw Elba"
    print(solution.isPalindrome2(test_str7))  # Output: True

    test_str8 = "12321"
    print(solution.isPalindrome2(test_str8))  # Output: True

    test_str9 = "12345"
    print(solution.isPalindrome2(test_str9))  # Output: False
