class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to store the opening brackets
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's non-empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # If the top element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # The stack should be empty if all the brackets are closed correctly
        return not stack







    



  

