#!/bin/bash

rm -rf *.out

sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "100KB" "500KB" "1MB" "10MB")
for s in "${sizes[@]}"
do
	for i in {1..100}
	do
		./greeter_client $s".txt" >> grpc-$s".out"
	done
	awk 'NR % 2 == 1' "grpc-"$s".out" > $s"-grpc.out"
	sort -n $s"-grpc.out" | awk -f median.awk >> "grpc-benchmark.result"
done
