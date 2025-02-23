import sys

class BinaryConverter:
    def __init__(self, binary_str):
        self.binary_str = binary_str
    
    def is_valid_binary(self):
        return all(digit in ('0', '1') for digit in self.binary_str)
    
    def to_decimal(self):
        if not self.is_valid_binary():
            return None
        decimal = 0
        for digit in self.binary_str:
            decimal = decimal * 2 + int(digit)
        return decimal
    
    def to_hex(self):
        decimal = self.to_decimal()
        if decimal is None:
            return "Invalid binary input"
        
        hex_chars = "0123456789ABCDEF"
        hex_str = ""
        while decimal > 0:
            hex_str = hex_chars[decimal % 16] + hex_str
            decimal //= 16
        
        return hex_str if hex_str else "0"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid input")
    else:
        converter = BinaryConverter(sys.argv[1])
        print(converter.to_hex())
