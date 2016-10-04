#!/bin/bash

rm -rf *.out

sizes=("1" "8" "16" "64" "128" "256" "512" "1024" "2048" "10240")
#sizes=("1MB" "2MB" "3MB" "4MB" "5MB" "6MB" "8MB" "9MB")
for s in "${sizes[@]}"
do
	for i in {1..100}
	do
		./route_guide_client $s >> grpc-$s".out"
	done
	awk 'NR % 3 == 0' "grpc-"$s".out" > $s"-grpc.out"
	sort -n $s"-grpc.out" | awk -f median.awk >> "grpc-benchmark-client-streaming.result"
done
