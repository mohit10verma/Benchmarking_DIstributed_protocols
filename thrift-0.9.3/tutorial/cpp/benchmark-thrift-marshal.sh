#!/bin/bash

rm -rf *.out

sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "100KB" "500KB" "1MB" "2MB" "3MB" "4MB" "5MB" "10MB")
#sizes=("1MB" "2MB" "3MB" "4MB" "5MB" "6MB" "8MB" "9MB")
for s in "${sizes[@]}"
do
	for i in {1..100}
	do
		sudo ./TutorialClient  $s".txt" >> thrift-$s".out"
	done
	#awk 'NR % 2 == 0' "thrift-"$s".out" > $s"-thrift.out"
	sort -n "thrift-"$s".out" | head -n 1 # >> "thrift-marshal.result"
done
