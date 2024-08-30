'''
LinkedList Problem
Practice Counter:

Merge Two Sorted Linked Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []

'''


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use technique of creating dummy node, so you don't have to worry about the edge case of inserting into an empty list
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:  # if list1 < list2, set tail.next to list1
                tail.next = list1
                list1 = list1.next  # move list1 pointer to the next node
            else:  # otherwise, set tail.next to list2
                tail.next = list2
                list2 = list2.next  # move list2 pointer to the next node
            tail = tail.next  # move the tail pointer to the next node
        
        # If one list is empty, point tail.next to the rest of the other list
        tail.next = list1 or list2

        return dummy.next  # return the merged list starting from dummy.next


# Helper functions to create and print linked lists for testing

# Function to create a linked list from a Python list
def create_linked_list(lst):
    if not lst:  # Check if the list is empty
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to convert a linked list to a Python list for easy verification
def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

if __name__ == "__main__":
    solution = Solution()


    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 5])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 5]

    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_head))  # Output: [0]

    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_head))  # Output: []

    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 4])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_head))  # Output: [1, 2, 4, 5]
