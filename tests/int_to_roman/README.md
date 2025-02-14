# Testy

Pro otestování funkčnosti spusťte následující příkazy v adresáři `dir`:


1. Neplatné vstupy:
```
python3 int_to_roman.py -2
python3 int_to_roman.py 0
python3 int_to_roman.py 4000
```
2. Nečíselný vstup: 
```
python3 int_to_roman.py ahoj
```
3. Více než 2 zadané argumenty: 
```
python3 int_to_roman.py 25 2
```
4. Platné vstupy:
```
python3 int_to_roman.py 25
python3 int_to_roman.py 444
```