#!/bin/bash
if [[ "$1" == "" ]]; then
    set -x #echo on
    rm -rf UDPEchoClient
    rm -rf UDPEchoServer
    g++ -o UDPEchoClient UDPEchoClient.cpp -O0
    g++ -o UDPEchoServer UDPEchoServer.cpp -O0
else
    rm -rf UDPEchoClient
    rm -rf UDPEchoServer
fi
