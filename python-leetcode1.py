print("Leetcode 1: Remove Duplicates from Sorted List")

class ListNode:
#  "def" means define, then fonction name, parameters, and a colon
#  "self" is a reference to the current instance of the class
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# "repr" means representation, it is a method that returns a string representation of the object
    def __repr__(self):
        # [] is a list, "str" converts the value to a string
        result = []
        current = self
        # while current is not None:
        while current:
            result.append(str(current.val))
            current = current.next
        # "->" is a string that joins the elements of the list with "->"
        return "->".join(result)

# I wrote this part by myself in C#, then converted it to Python
def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Test results case in LeetCode:
list1 = ListNode(1, ListNode(1, ListNode(2)))
list2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

# Results accepted in LeetCode:
print(delete_duplicates(list1))
print(delete_duplicates(list2))