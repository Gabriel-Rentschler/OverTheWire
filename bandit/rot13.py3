#!bin/python3

frase = input('Escreva String ROT13: ');

for char in frase:
    convert = ord(char);
    
    if convert > 96 and convert < 123:
        convert = convert + 13;

        if convert > 122:
            sobra = convert - 122;
            convert = 96 + sobra;
    elif convert > 64 and convert < 91:
        convert = convert + 13;

        if convert > 90:
            sobra = convert - 90;
            convert = 64 + sobra;
    
    char = chr(convert);
    print(char, end="");
