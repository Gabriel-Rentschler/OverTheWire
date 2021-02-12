#!/bin/python3

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

counter=[letters]*2;

counter[0][0]=1;
counter[1][0]=2;
counter[0][0]=3;

print(counter[0][0]);
print(counter[1][0]);
print(counter[0][1]);
print(counter[1][1]);
