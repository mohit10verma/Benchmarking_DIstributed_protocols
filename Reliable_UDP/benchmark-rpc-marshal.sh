#!/bin/bash

rm -rf *.out

#sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "60KB")
sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "100KB" "500KB" "1MB" "2MB" "3MB" "4MB" "5MB" "10MB")
for s in "${sizes[@]}"
do
	for i in {1..100}
	do
		./UDPEchoClient $s".txt" >> $s".out"
	done
	#awk 'NR % 5 == 1' "my-rpc-"$s".out" > $s".out"
	sort -n $s".out" | head -n 1 
done
