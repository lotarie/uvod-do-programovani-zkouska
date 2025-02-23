import sys

class IntegerToRomanConverter:
    def __init__(self, number):
        self.number = number
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    def is_valid_number(self):
        try:
            self.number = int(self.number)
            return 0 < self.number < 4000
        except ValueError:
            return False
    
    def to_roman(self):
        if not self.is_valid_number():
            return "Invalid input"
        
        result = ""
        number = self.number
        
        for value, symbol in self.roman_numerals:
            while number >= value:
                result += symbol
                number -= value
        
        return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
    else:
        converter = IntegerToRomanConverter(sys.argv[1])
        print(converter.to_roman())
