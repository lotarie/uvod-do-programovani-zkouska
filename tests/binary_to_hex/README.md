# Testy

Pro otestování funkčnosti spusťte následující příkazy v adresáři `dir`:

1. Číslo v jiné než dvojkové soustavě:
```
python3 binary_to_hex.py 00021 
```

2. Nečíselný vstup:
```
python3 binary_to_hex.py ahoj 
```
3. Více než 2 zadané argumenty: 
```
python3 binary_to_hex.py 10 001 
```
4. Platné vstupy 
```
python3 binary_to_hex.py 0011100
python3 binary_to_hex.py 0
```