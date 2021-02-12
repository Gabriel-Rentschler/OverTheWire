#!/bin/python3

string = input("String to code/decode: ");

for n in string:
    n = ord(n);
    
    #Check for uppercase letters
    if(n > 64 and n < 91):
        n += 13;

        if(n > 90):
            sobra = n - 90;
            n = 64 + sobra;

    #Check for lowercase letters
    if(n > 96 and n < 123):
        n += 13;

        if(n > 122):
            sobra = n - 122;
            n = 96 + sobra;
    print(chr(n), end="");
