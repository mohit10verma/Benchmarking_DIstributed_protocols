#!/bin/bash
set -x #echo on
rm UDPEchoClient
rm UDPEchoServer
g++ -o UDPEchoClient UDPEchoClient.cpp -O3
g++ -o UDPEchoServer UDPEchoServer.cpp -O3
