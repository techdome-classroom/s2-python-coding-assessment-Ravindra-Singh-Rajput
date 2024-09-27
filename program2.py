class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map each Roman numeral to its corresponding integer value
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

        # Iterate over the string in reverse order
        for char in reversed(s):
            current_value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
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



