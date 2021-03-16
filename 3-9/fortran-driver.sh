!/bin/bash

# we are supoed to make shell code for our fortan that we were running manully earlier 
# this shoul have a loop, the fortran comands and 


for i in (example_ome.py + example_vec.py)
do
    gfortran -O3 -o vectorq.exe vectorq.f
	gfortran -O3 -o omegainv.exe omegainv.f
	./vectorq.exec
	./omegainv.exec
done