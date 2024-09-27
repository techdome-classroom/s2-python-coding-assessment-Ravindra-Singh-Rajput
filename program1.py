class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        
        for char in s:
        
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







    



  

