#!/bin/python3

string=input('Text to replace: ');
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
counter=0;
for l in letters:
    l = input('Write the replace for ' + l + ': ');
    letters[counter] = l;
    counter += 1;
for n in string:
    if n != ' ':
        if n == 'A': 
            n = letters[0];
        elif n == 'B': 
            n = letters[1];
        elif n == 'C': 
            n = letters[2];
        elif n == 'D': 
            n = letters[3];
        elif n == 'E': 
            n = letters[4];
        elif n == 'F': 
            n = letters[5];
        elif n == 'G': 
            n = letters[6];
        elif n == 'H': 
            n = letters[7];
        elif n == 'I': 
            n = letters[8];
        elif n == 'J': 
            n = letters[9];
        elif n == 'K': 
            n = letters[10];
        elif n == 'L': 
            n = letters[11];
        elif n == 'M': 
            n = letters[12];
        elif n == 'N': 
            n = letters[13];
        elif n == 'O': 
            n = letters[14];
        elif n == 'P': 
            n = letters[15];
        elif n == 'Q': 
            n = letters[16];
        elif n == 'R': 
            n = letters[17];
        elif n == 'S': 
            n = letters[18];
        elif n == 'T': 
            n = letters[19];
        elif n == 'U':
            n = letters[20];
        elif n == 'V': 
            n = letters[21];
        elif n == 'W': 
            n = letters[22];
        elif n == 'X':
            n = letters[23];
        elif n == 'Y':
            n = letters[24];
        elif n == 'Z':
            n = letters[25];
    print(n, end='');
