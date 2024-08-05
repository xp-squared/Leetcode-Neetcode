'''
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        # checking lengths takes O(1) time
        if len(s) != len(t):
            # Anagrams have to be the same length to be true!
            return False
        # The sorted function treats strings like a list and iterates through them.
        # We compare them both to see if they are anagrams of each other.
        # sorted function takes O(NlogN) time, to compare the elements when returning takes N amount of time
        # our time complexity is O(NlogN)
        return sorted(s) == sorted(t)

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    s1 = "dog"
    t1 = "cat"
    s2 = "angel"
    t2 = "glean"

    result1 = solution.isAnagram1(s1, t1)
    print(f"Are '{s1}' and '{t1}' anagrams? {result1}")
    result2 = solution.isAnagram1(s2, t2)
    print(f"Are '{s2}' and '{t2}' anagrams? {result2}")
