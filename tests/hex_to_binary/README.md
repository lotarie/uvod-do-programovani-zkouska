# Testy

Pro otestování funkčnosti spusťte následující příkazy v adresáři `dir`:


1. Neplatné vstupy:
```
python3 hex_to_binary.py ahoj 
python3 hex_to_binary.py 65vb
```
2. Více než 2 zadané argumenty: 
```
python3 hex_to_binary.py 5f 123 
```
3. Platné vstupy:
```
python3 hex_to_binary.py 65b
python3 hex_to_binary.py 0
```