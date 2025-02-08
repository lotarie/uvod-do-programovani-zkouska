#Prevod cisla na rimske cislice a zpet
import sys

def int_to_roman(number):
    try:
        number=int(number)
        if not (0 < number < 4000):
            return "Neplatny vstup."
        
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        for value, symbol in roman_numerals:
            while number >= value:
                result += symbol
                number -= value
        
        return result
    except:
        return "Neplatny vstup."
    
if len(sys.argv) != 2:
    print("Byl zadan jiny pocet argumentu")
else:
    print(int_to_roman(sys.argv[1]))





