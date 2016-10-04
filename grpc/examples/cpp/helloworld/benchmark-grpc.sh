#!/bin/bash

rm -rf *.out
rm -rf grpc-benchmark.result

sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "100KB" "500KB" "1MB" "2MB" "3MB" "4MB" "5MB" "10MB")
#sizes=("1MB" "2MB" "3MB" "4MB" "5MB" "6MB" "8MB" "9MB")
for s in "${sizes[@]}"
do
	sshpass -p Mohit@123456 ssh cs838fall2016group123.eastus.cloudapp.azure.com "cd /home/ubuntu/grpc/examples/cpp/helloworld/; ./greeter_server $s\".txt\" < /dev/null >~/server.log 2>&1 &"
	sleep 2
	for i in {1..10}
	do
		./greeter_client $s".txt" >> grpc-$s".out"
	done
	sshpass -p Mohit@123456 ssh cs838fall2016group123.eastus.cloudapp.azure.com "ps aux | grep server | awk '{print \$2}' | xargs kill -9"
	awk 'NR % 2 == 1' "grpc-"$s".out" > $s"-grpc.out"
	sort -n $s"-grpc.out" | head -n 1 >> "grpc-benchmark.result"
done
