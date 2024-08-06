'''
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity of sorting all string is NLogN
        # Have to do that M amount of time
        # time complexity of that is O(M*NLogN)


        # there is a better way of doing it though
        # there are 26 letters
        # in a string count how many characters of each is in it
        # use hashmap, key is our number of letters for each letter and value is our anagram
        # O(M * N) M = strings were given, N = length of string

        res = defaultdict(list) # mapping charCount to list of anagrams, this is our hashmap
        # using the list inside of defaultdict provides a default value for missing keys

        for s in strs:
            count = [0] * 26 # a to z
            # a = 0
            # b = 0
            # c = 0

            for c in s:
                count[ord(c) - ord("a")] += 1 # this gives us the value of the letter, remember ord changes a character to its integer representation
                
            # Convert the count list to a tuple and use as a key
            res[tuple(count)].append(s)
        return res.values()
    
if __name__ == "__main__":
    solution = Solution()
    

    strs1 = ["act","pots","tops","cat","stop","hat"]
    print(solution.groupAnagrams(strs1))  # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    
    strs2 = ["x"]
    print(solution.groupAnagrams(strs2))  # Output: [["x"]]
    
    # Test case 3
    strs3 = [""]
    print(solution.groupAnagrams(strs3))  # Output: [[""]]