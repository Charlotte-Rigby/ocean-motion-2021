#!/bin/bash
 cd ../2-25

 STRING="START"
 echo $STRING

 gfortran -O3 -o vectorq.exe vectorq.f
 gfortran -O3 -o omegainv.exe omegainv.f

while read p; do
  python example_vec.py $p
  
  ./vectorq.exec
  ./omegainv.exec
done <date_list.txt

STRING="Done"
echo $STRING