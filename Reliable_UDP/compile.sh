#!/bin/bash
if [[ "$1" == "" ]]; then
    set -x #echo on
    rm -rf UDPEchoClient
    rm -rf UDPEchoServer
    g++ -o UDPEchoClient UDPEchoClient.cpp -O3
    g++ -o UDPEchoServer UDPEchoServer.cpp -O3
else
    rm -rf UDPEchoClient
    rm -rf UDPEchoServer
fi
