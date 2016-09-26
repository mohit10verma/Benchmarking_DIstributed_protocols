#!/bin/bash
set -x #echo on
rm a.out
g++ -o a.out L1cachetime.cpp -O0
#g++ -o UDPEchoServer UDPEchoServer.cpp -O3
