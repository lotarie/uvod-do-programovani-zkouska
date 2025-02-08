
import sys

def roman_to_int(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    count = 0
    prev_char = ""
    
    for char in reversed(roman):
        value = roman_values.get(char, 0)
        if value == 0:
            return "Neplatny vstup."
        
        if char == prev_char:
            count += 1
            if count == 3:
                return "Neplatny vstup: vice nez tri stejne rimske cislice za sebou."
        else:
            count = 0
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
        prev_char = char
    
    return total

if len(sys.argv) != 2:
    print("Byl zadan jiny pocet argumentu")
else:
    print(roman_to_int(sys.argv[1]))