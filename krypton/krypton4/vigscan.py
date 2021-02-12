#!/bin/python3

string=input('Put string: ');
key_len=input('Key length: ');
counter=0;
len_counter=1;
while len_counter <= int(key_len):
    print('Key letter '+ str(len_counter) + ': ');
    len_max=len_counter;
    final_string='';
    for n in string:
        if n != ' ':
            counter+=1;

            if counter == len_max:
                final_string += n;
                len_max += 6;

    counter=0;
    len_counter += 1;
    print(final_string);

