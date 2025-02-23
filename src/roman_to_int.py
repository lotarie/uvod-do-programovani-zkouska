import sys

class RomanToIntConverter:
    def __init__(self, roman):
        self.roman = roman
        self.roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    
    def is_valid_roman(self):
        for char in self.roman:
            if char not in self.roman_values:
                return False
        return True
    
    def to_integer(self):
        if not self.is_valid_roman():
            return "Invalid input."
        
        total = 0
        prev_value = 0
        count = 0
        prev_char = ""
        
        for char in reversed(self.roman):
            value = self.roman_values.get(char, 0)
            
            if char == prev_char:
                if char in {"V", "L", "D"}:
                    return "Invalid input."
                count += 1
                if count == 3:
                    return "Invalid input: more than 3 same roman numerals in a row"
            else:
                count = 0
            
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
            prev_char = char
        
        return total

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
    else:
        converter = RomanToIntConverter(sys.argv[1])
        print(converter.to_integer())
