#!/bin/python3

string='KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS';
isRight=False;
key=1;

while isRight==False:
    for n in string:
        n = ord(n);

        #Check for uppercase letters
        if(n > 64 and n < 91):
            n -= int(key);

            if(n < 65):
                sobra = 65 - n;
                n = 91 - sobra;

        #Check for lowercase letters
        if(n > 96 and n < 123):
            n -= int(key);

            if(n < 97):
                sobra = 97 - n;
                n = 123 - sobra;
        print(chr(n), end="");

    choice = input('Does this makes sense? (y/n)');

    if choice=='y':
        isRight==True;
    else:
        key+=1;
