#!/bin/python3

string=input('Paste the message: ');
key=input('Paste the key: ');

key_final=[];

for x in key:
    x = ord(x) - 64;
    key_final.append(x);

key_counter=0;
for n in string:
    if n != ' ':
        n = ord(n) - 64;

        if key_counter >= (len(key)):
            key_counter = 0;

        n -= (key_final[key_counter]-1);
        key_counter += 1;

        if n < 1:
            n += 26;
    
        n += 64;
        print(chr(n), end='');
        
