#!/bin/python3

string=input('Paste the coded text: ');
letters=[0]*26;
counter=[0]*26;
letter_text=['E','T','A','O','I','N','S','H','R','D','L','U','M','N','O','P','Q','R','S','T','U','F','Z','Q','X','J'];
total=0;
ordletter=0;
repeat=0;
lastletter='';

for n in string:
    if n != ' ':
        total += 1;

        if lastletter == n:
            repeat = 1;
        else:
            repeat = 0;

        lastletter = n;

        if n == 'A':
            letters[0] += 1;
            counter[0] += repeat;
        elif n == 'B':
            letters[1] += 1;
            counter[1] += repeat;
        elif n == 'C':
            letters[2] += 1;
            counter[2] += repeat;
        elif n == 'D':
            letters[3] += 1;
            counter[3] += repeat;
        elif n == 'E':
            letters[4] += 1;
            counter[4] += repeat;
        elif n == 'F':
            letters[5] += 1;
            counter[5] += repeat;
        elif n == 'G':
            letters[6] += 1;
            counter[6] += repeat;
        elif n == 'H':
            letters[7] += 1;
            counter[7] += repeat;
        elif n == 'I':
            letters[8] += 1;
            counter[8] += repeat;
        elif n == 'J':
            letters[9] += 1;
            counter[9] += repeat;
        elif n == 'K':
            letters[10] += 1;
            counter[10] += repeat;
        elif n == 'L':
            letters[11] += 1;
            counter[11] += repeat;
        elif n == 'M':
            letters[12] += 1;
            counter[12] += repeat;
        elif n == 'N':
            letters[13] += 1;
            counter[13] += repeat;
        elif n == 'O':
            letters[14] += 1;
            counter[14] += repeat;
        elif n == 'P':
            letters[15] += 1;
            counter[15] += repeat;
        elif n == 'Q':
            letters[16] += 1;
            counter[16] += repeat;
        elif n == 'R':
            letters[17] += 1;
            counter[17] += repeat;
        elif n == 'S':
            letters[18] += 1;
            counter[18] += repeat;
        elif n == 'T':
            letters[19] += 1;
            counter[19] += repeat;
        elif n == 'U':
            letters[20] += 1;
            counter[20] += repeat;
        elif n == 'V':
            letters[21] += 1;
            counter[21] += repeat;
        elif n == 'W':
            letters[22] += 1;
            counter[22] += repeat;
        elif n == 'X':
            letters[23] += 1;
            counter[23] += repeat;
        elif n == 'Y':
            letters[24] += 1;
            counter[24] += repeat;
        elif n == 'Z':
            letters[25] += 1;
            counter[25] += repeat;

print('Frequency of the letters:');
for x in letters:
    x = x/total;
    x = x*100;
    letters[ordletter]=x;
    finletter = 65+ordletter;
    print('Letter ' + chr(finletter) + ': ' + str(x) + '%');
    ordletter += 1;

ordletter = 0;

print('');
print('Times a letter is double: ')
for y in counter:
    counter[ordletter]=y;
    finletter = 65+ordletter;
    print('Letter ' + chr(finletter) + ' as a pair: ' + str(y) + ' times.');
    ordletter +=1;

choice = input('Proceed with reversing the text? (y/n)');

if choice == 'y':
    letters_sorted = sorted(letters, reverse=True);
    counter_sorted = sorted(counter, reverse=True);

    print('Using the default ETAOIN SHRDLU replacement...');

        for n in string:
            if n != ' ':
                if n == 'A':
                    etaoin(letters[0], letters_sorted);
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

def etaoin(letters_, letters_sorted_):
    count=0;
    for x in letters_sorted_:
        if x == letters_:
            return letter_text[count];    

        count += 1;

