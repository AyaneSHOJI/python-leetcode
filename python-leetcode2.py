print("Leetcode 2: Valid Parentheses")

class String:
    def __init__(self, s=""):
        self.s = s

    def __repr__(self):
        return self.s

# This solution was written with the help of copilot and tutorials
# I wanted to check the target char with the next char and the char at the same index from the end, but it didn't work 
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
    
        # create a dictionary to map opning brackets to closing brackets
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        # create a stack to keep track of opening brackets
        stack = []       
        # Iterate through the string
        for c in s:
            # If the character is an open bracket, push it onto the stack
            if c in bracket_map:
                stack.append(c)
            # If the character is a close bracket, check if it is the corresponding closing bracket for the top element of the stack
            elif not stack or bracket_map[stack[-1]] != c:
                return False
            # If it is a valid closing bracket, pop the top element from the stack
            else:
                stack.pop()
        
        # If the stack is empty at the end, then the string is valid
        return not stack

# Test cases
s = "([)]"
s2 = "([])"   
print(isValid(s))  # Output: False
print(isValid(s2))  # Output: True