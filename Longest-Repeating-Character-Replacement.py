'''
Longest Repeating Substring With Replacement
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window problem

        # you are given a string like XYYX
        # as well a integer k
        # you can shoose any chracter of the string and change it to any other UPPERCASE character
        # want to create the longest possible substring with the same letter
        # changing XYYX to XXXX would give us a result of 4
        # This takes O(N * 26) time

        count = {} # hash map to count occurence of each character
        # if the current window length - count of most frequent letter 
        # is less than or equal to k means our current window is valid
        # if not we move our left pointer
        res = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # for string[r] we are adding to its count in the hashmap, if it is not in there it is automatically 0
            
            while (r - l + 1) - max(count.values()) > k: 
                # to explain the above line, if your current window length - most frequent letter is greater than k we have to move our window
                count[s[l]] -= 1 # decrementing the character at our left most position in the hash map so we have valid counts
                l += 1
            res = max(res, r - l + 1) # result from previous results and current size of the window + 1
        return res


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    print(solution.characterReplacement("AABABBA", 1))  # Output: 4

    print(solution.characterReplacement("ABAB", 2))  # Output: 4

    print(solution.characterReplacement("AAAA", 2))  # Output: 4

    print(solution.characterReplacement("ABDDFFG", 3))  # Output: 5

