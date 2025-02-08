import sys

def hex_to_binary(hex_str):
    try:
        decimal = 0
        hex_chars = "0123456789ABCDEF"
        for digit in hex_str.upper():
            if digit not in hex_chars:
                return "Neplatny hexadecimalni vstup"
            decimal = decimal * 16 + hex_chars.index(digit)
        
        binary_str = ""
        while decimal > 0:
            binary_str = str(decimal % 2) + binary_str
            decimal //= 2
        
        return binary_str if binary_str else "0"
    except:
        return "Neplatny hexadecimalni vstup"
    
if len(sys.argv) != 2:
    print("Byl zadan jiny pocet argumentu")
else:
    print(hex_to_binary(sys.argv[1]))