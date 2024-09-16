from collections import deque
class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        
        roman_digits = []
        
        # loop through the list of tuples 
        for value, symbol in digits:
            if num==0:
                break
            #quotient, remainder = divmod(dividend, divisor)
            count, num = divmod(num, value)
            
            # append count number of copies of symbol to the roman_digits
            roman_digits.append(symbol*count)
        
        return "".join(roman_digits)
            
        