#!/bin/python3

choice = input('To encode press (e) and to decode press (d): ');

string = input('Write the message: ');
key = input('Write the key: ');

if choice == 'd':
    #Decode
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
else:
    #Encode
    for n in string:
        n = ord(n);
    
        #Check for uppercase letters
        if(n > 64 and n < 91):
            n += int(key);

            if(n > 90):
                sobra = n - 90;
                n = 64 + sobra;

        #Check for lowercase letters
        if(n > 96 and n < 123):
            n += int(key);

            if(n > 122):
                sobra = n - 122;
                n = 96 + sobra;
        print(chr(n), end="");
