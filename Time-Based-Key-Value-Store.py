'''
This is a binary search problem

Time Based Key-Value Store
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"

ALL THE TIMESTAMPS OF SET ARE STRICTLY INCREASING!!!
'''

class TimeMap:
    # we are gonna have a key value and a list of values associated with the key
    # that list is a pair of values
    # Key : Values <val, timeStamp>
    # "foo" : [["bar",1],["bar",2]]

    # if you don't find exact match in key-value store you return the most recent one that is less than it
    def __init__(self):
        self.keyStore = {}  # key = string, value = list of [string, timestamp]
        # initializing a dictionary in the constructor 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:  # if the key is not in the map
            self.keyStore[key] = []  # we want to insert the key into the map
        self.keyStore[key].append([value, timestamp])  # if it does exist we just insert at key's location

    def get(self, key: str, timestamp: int) -> str:
        # Returns the most recent value of key if set was previously called on it
        # based on most recent timestamp compared to one given, if user gives 3 and 1 was most recent we go to 1
        # do this in binary search 
        
        res = ""  # if the key does not exist we return an empty string

        # This line is accessing the keyStore dictionary and trying to retrieve
        # the list of values associated with the given key. If the key is not 
        # found in the dictionary, it returns an empty list [].
        # foo : [["bar",1],["bar",2],["bar",3],["bar",4]]
        values = self.keyStore.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:  # [1] is used to get that middle value's timestamp, if it is less than the one we are searching for, we move the left pointer up to get more accurate
                res = values[m][0]  # this is a possible valid value, since the result has to be either the target or the most recent one less than the target 
                l = m + 1
            else:  # invalid to assign this to the result
                # we do not need to assign something greater to the result; it is either equal or less
                r = m - 1
        return res


# Example test cases
if __name__ == "__main__":
    timeMap = TimeMap()

    # Test case 1
    timeMap.set("foo", "bar", 1)  # store the key "foo" with value "bar" at timestamp 1
    print(timeMap.get("foo", 1))  # return "bar"
    print(timeMap.get("foo", 3))  # return "bar", because the closest time <= 3 is 1

    # Test case 2
    timeMap.set("foo", "bar2", 4)  # store the key "foo" with value "bar2" at timestamp 4
    print(timeMap.get("foo", 4))  # return "bar2"
    print(timeMap.get("foo", 5))  # return "bar2", because the closest time <= 5 is 4
