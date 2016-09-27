#!/bin/bash

rm -rf *.out

sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "60KB")
for s in "${sizes[@]}"
do
	for i in {1..100}
	do
		./UDPEchoClient localhost $s".txt" >> my-rpc-$s".out"
	done
	awk 'NR % 5 == 1' "my-rpc-"$s".out" > $s".out"
	sort -n $s".out" | awk -f median.awk
done
