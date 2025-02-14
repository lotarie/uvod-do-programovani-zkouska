# Testy

Pro otestování funkčnosti spusťte následující příkazy v adresáři `dir`:


1. Neplatné vstupy:
```
python3 roman_to_int.py cd
python3 roman_to_int.py 0
```
2. Více než 3 římské číslice za sebou (+kontrola cislic V,L,D): 
```
python3 roman_to_int.py LLLL
python3 roman_to_int.py VV
```
3. Více než 2 zadané argumenty: 
```
python3 roman_to_int.py CD X
```
4. Platné vstupy:
```
python3 roman_to_int.py CD
python3 roman_to_int.py IV

```