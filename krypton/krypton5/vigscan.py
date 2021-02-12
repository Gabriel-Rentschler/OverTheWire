#!/bin/python3

string=input('Put string: ');
key='';
key_length=1;
counter=0;
len_counter=1;
isRunning = True;

#loop to run until the program sees that the key is repeating
while isRunning == True:
    len_max= len_counter;
    final_string='';
    letters=[0]*26;
    total=0;

    #count the letters in the position of the char in the key
    for n in string:
        if n != ' ':
            counter+=1;

            if counter == len_max:
                final_string += n;
                len_max += key_length;
                #Frequency analysis to see the letter which appears the most
                total += 1;
                
                if n == 'A': letters[0] += 1;
                elif n == 'B': letters[1] += 1;
                elif n == 'C': letters[2] += 1;
                elif n == 'D': letters[3] += 1;
                elif n == 'E': letters[4] += 1;
                elif n == 'F': letters[5] += 1;
                elif n == 'G': letters[6] += 1;
                elif n == 'H': letters[7] += 1;
                elif n == 'I': letters[8] += 1;
                elif n == 'J': letters[9] += 1;
                elif n == 'K': letters[10] += 1;
                elif n == 'L': letters[11] += 1;
                elif n == 'M': letters[12] += 1;
                elif n == 'N': letters[13] += 1;
                elif n == 'O': letters[14] += 1;
                elif n == 'P': letters[15] += 1;
                elif n == 'Q': letters[16] += 1;
                elif n == 'R': letters[17] += 1;
                elif n == 'S': letters[18] += 1;
                elif n == 'T': letters[19] += 1;
                elif n == 'U': letters[20] += 1;
                elif n == 'V': letters[21] += 1;
                elif n == 'W': letters[22] += 1;
                elif n == 'X': letters[23] += 1;
                elif n == 'Y': letters[24] += 1;
                elif n == 'Z': letters[25] += 1;
    
    frequent_letter = 0;
    counter = 0;
    #Putting the number of apparitions in a percentage
    for x in letters:
        x = x/total;
        x = x*100;
        letters[counter]=x;
        counter += 1;
    #Checking for the most frequent letter    
    pos_counter = 0;
    last_letter = 0;
    for y in letters:
        if y > last_letter:
            last_letter = y;
            frequent_letter = pos_counter;
        pos_counter += 1;
    
    #Finding the most probable letter of the key
    if frequent_letter <= 5:
        frequent_letter += 26;
    key += chr((frequent_letter) + 61);

    if len_counter == key_length:
        len_counter = 0;
        print(key);

        choice=input('Is this right? (y/n)');
        if choice == 'y':
            isRunning = False;
        elif choice == 'n':
            key_length += 1;
            key='';

    len_counter += 1;
    counter = 0;
