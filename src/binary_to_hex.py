#Prevod cisla c, c=Z+, z dvojkove do setnactkove soustavy
import sys

def binary_to_hex(binary_str):
    try:
        decimal = 0
        for digit in binary_str:
            if digit not in ('0', '1'):
                return "Neplatny binarni vstup."
            decimal = decimal * 2 + int(digit)
        
        hex_chars = "0123456789ABCDEF"
        hex_str = ""
        while decimal > 0:
            hex_str = hex_chars[decimal % 16] + hex_str
            decimal //= 16
        
        return hex_str if hex_str else "0"
    except:
        return "Neplatny binarni vstup"

if len(sys.argv) != 2:
    print("Byl zadan jiny pocet argumentu")
else:
    print(binary_to_hex(sys.argv[1]))
    



