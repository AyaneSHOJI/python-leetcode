print("Leetcode 3: Reverse Linked List")

# This solution was written with the help of copilot and tutorials
# I wanted to use stack

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        
        # create a stcak to store the values of the linked list
        stack = []

        # push all the values of the linked list onto the stack
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        # pop all the values from the stack and create a new linked list
        dummy = ListNode()
        curr = dummy
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return dummy.next 

# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to convert linked list to list (for printing)
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
head = list_to_linkedlist([1,2,3,4,5])
head2 = list_to_linkedlist([1,2])
head3 = list_to_linkedlist([])

print(linkedlist_to_list(Solution().reverseList(head)))   # Output: [5,4,3,2,1]
print(linkedlist_to_list(Solution().reverseList(head2)))  # Output: [2,1]
print(linkedlist_to_list(Solution().reverseList(head3)))  # Output: []