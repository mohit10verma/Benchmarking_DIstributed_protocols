#!/bin/bash

rm -rf *.out
#rm -rf thrift-benchmark.result

sizes=("1B")
#sizes=("1B" "8B" "16B" "64B" "128B" "256B" "512B" "1KB" "2KB" "10KB" "50KB" "100KB" "500KB" "1MB" "2MB" "3MB" "4MB" "5MB" "10MB")
#sizes=("1MB" "2MB" "3MB" "4MB" "5MB" "6MB" "8MB" "9MB")
for s in "${sizes[@]}"
do
	#same-machine
	sshpass -p Mohit@123456 ssh localhost "cd /home/ubuntu/thrift-0.9.3/tutorial/cpp; sudo ./TutorialServer $s\".txt\" < /dev/null >~/server.log 2>&1 &"
	sleep 2
	sudo ./TutorialClient $s".txt" localhost >> "thrift-"$s".out"
	sshpass -p Mohit@123456 ssh localhost "ps aux | grep Server | awk '{print \$2}' | xargs sudo kill -9"
	cat "thrift-"$s".out" > "thrift-rtt-same.result"
	
	rm -rf *.out
	#diff-machine
	sshpass -p Mohit@123456 ssh cs838fall2016group123.eastus.cloudapp.azure.com "cd /home/ubuntu/thrift/thrift-0.9.3/tutorial/cpp; sudo ./TutorialServer $s\".txt\" < /dev/null >~/server.log 2>&1 &"
	sleep 2
	sudo ./TutorialClient $s".txt" cs838fall2016group123.eastus.cloudapp.azure.com >> "thrift-"$s".out"
	sshpass -p Mohit@123456 ssh cs838fall2016group123.eastus.cloudapp.azure.com "ps aux | grep Server | awk '{print \$2}' | xargs sudo kill -9"
	cat "thrift-"$s".out" > "thrift-rtt-diff.result"
done
