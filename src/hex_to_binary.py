import sys

class HexConverter:
    def __init__(self, hex_str):
        self.hex_str = hex_str.upper()
        self.hex_chars = "0123456789ABCDEF"
    
    def is_valid_hex(self):
        return all(digit in self.hex_chars for digit in self.hex_str)
    
    def to_decimal(self):
        if not self.is_valid_hex():
            return None
        decimal = 0
        for digit in self.hex_str:
            decimal = decimal * 16 + self.hex_chars.index(digit)
        return decimal
    
    def to_binary(self):
        decimal = self.to_decimal()
        if decimal is None:
            return "Invalid hexadecimal input"
        
        binary_str = ""
        while decimal > 0:
            binary_str = str(decimal % 2) + binary_str
            decimal //= 2
        
        return binary_str if binary_str else "0"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
    else:
        converter = HexConverter(sys.argv[1])
        print(converter.to_binary())
