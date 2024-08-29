'''
LinkedList Problem
Practice Counter:

Reverse a Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
'''


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity O(n) 
        # Memory complexity O(1)
        prev = None
        current = head
        
        while current:  # while current is not None
            temp = current.next  # grabbing the next element and holding it in temp
            current.next = prev  # reversing the link
            prev = current  # move prev to the current node
            current = temp  # move to the next node
        return prev  # prev becomes the new head of the reversed list


# Helper functions to test the reverseList method

# Function to create a linked list from a list
def create_linked_list(lst):
    if not lst:  # Check if the list is empty
        return None  # Return None for an empty list
    
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to convert linked list to a Python list for easy verification
def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

if __name__ == "__main__":
    solution = Solution()

    head1 = create_linked_list([0, 1, 2, 3])
    reversed_head1 = solution.reverseList(head1)
    print(linked_list_to_list(reversed_head1))  # Output: [3, 2, 1, 0]

    head3 = create_linked_list([3, 2, 1, 0])
    reversed_head3 = solution.reverseList(head3)
    print(linked_list_to_list(reversed_head3))  # Output: [0, 1, 2, 3]
