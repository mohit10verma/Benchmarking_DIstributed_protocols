#!/bin/bash

rm -rf *.out 
j=1 
for i in {1..30}
do 
j=$(($j<<1))
	for i in {1..100} 
	do 
	sudo ./TutorialClient $j >> $s".out"
	done 
sort -n $s".out" | head -n 1
done
