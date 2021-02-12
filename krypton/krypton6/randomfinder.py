#!/bin/python3

string=input('Write the plain text: ');
cipher=input('Write the encoded text: ');

counter=0;
string_ord=[];
key='';

for x in string:
    string_ord.append(ord(x));

for y in cipher:
    print(ord(y) - string_ord[counter]);
    counter += 1;
    



