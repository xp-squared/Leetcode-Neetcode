'''
Sliding Window Problem
Longest Substring Without Duplicates
Practice counter: 1


Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    solution = Solution()

    s1 = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s1))  # Output: 3 ("abc")

    s2 = "bbbbb"
    print(solution.lengthOfLongestSubstring(s2))  # Output: 1 ("b")

    s3 = "pwwkew"
    print(solution.lengthOfLongestSubstring(s3))  # Output: 3 ("wke")

    s4 = ""
    print(solution.lengthOfLongestSubstring(s4))  # Output: 0 ("")

    s5 = "dvdf"
    print(solution.lengthOfLongestSubstring(s5))  # Output: 3 ("vdf")
