class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

    
        for char in reversed(s):
            current_value = roman_to_int[char]
            
        
            if current_value < prev_value:
                total -= current_value
            else:
                # Otherwise, add it
                total += current_value
            
            # Update prev_value to the current value
            prev_value = current_value

        return total

# Test cases
solution = Solution()
print(solution.romanToInt("III"))       # Output: 3
print(solution.romanToInt("LVIII"))     # Output: 58
print(solution.romanToInt("MCMXCIV"))   # Output: 1994



