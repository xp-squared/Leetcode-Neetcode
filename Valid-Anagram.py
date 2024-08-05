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
    
    def isAnagram2(self, s: str, t: str) -> bool:
        '''
        return Counter(s) == Counter(t)
        
        A Counter is a dict subclass for counting hashable objects. 
        It is a collection where elements are stored as dictionary 
        keys and their counts are stored as dictionary values. 
        Counts are allowed to be any integer value including zero or 
        negative counts.

        We basically did this in the code below, same thing but just using the counter function instead
        '''
        if len(s) != len(t):
            return False
        # this time we are going to use a hash map
        # time complexity is O(S + T), we have to iterate through both strings

        countS, countT = {},{}
        for i in range(len(s)):
            # count each occurence in both strings
            # s[i] is the key
            # we want to increment the count of the characters we see
            # we use the get function to get the key, if the key does not exist in the hashmap the default value returned is 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print()
    s1 = "dog"
    t1 = "cat"
    s2 = "angel"
    t2 = "glean"
    result1 = solution.isAnagram1(s1, t1)
    print(f"Are '{s1}' and '{t1}' anagrams? {result1}")
    result2 = solution.isAnagram1(s2, t2)
    print(f"Are '{s2}' and '{t2}' anagrams? {result2}")

    print()
    s3 = "rag"
    t3 = "bag"
    s4 = "earth"
    t4 = "heart"
    result3 = solution.isAnagram2(s3, t3)
    print(f"Are '{s3}' and '{t3}' anagrams? {result3}")
    result4 = solution.isAnagram2(s4, t4)
    print(f"Are '{s4}' and '{t4}' anagrams? {result4}")
