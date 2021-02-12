#!/bin/python3

string=input('Cipher text: ');
key=input('Key (each number separated by a SPACE): ');

key_tmp='';
counter = 0;
key_final=[];
for n in key:
    if n != ' ':
        key_tmp += n;
    else:
        key_final.append(int(key_tmp));
        key_tmp = '';

for x in string:
    x = ord(x) - key_final[counter];

    if x < 65:
        sobra = 64 - x;
        x = 90 - sobra;

    counter += 1;

    print(chr(x));
    if counter == (len(key_final)-1):
        counter = 0;

